import os
import sys
import json
import re
from pathlib import Path
import pandas as pd

def extract_text_from_telegram_field(text_field):
    """Mengekstrak teks murni dari field text Telegram export (string atau list)."""
    if isinstance(text_field, str):
        return text_field
    elif isinstance(text_field, list):
        full_text = []
        for part in text_field:
            if isinstance(part, str):
                full_text.append(part)
            elif isinstance(part, dict):
                full_text.append(part.get("text", ""))
        return "".join(full_text)
    return str(text_field or "")

def parse_telegram_json(json_path, output_csv="notifikasi_telegram_5000.csv"):
    if not os.path.exists(json_path):
        print(f"❌ File tidak ditemukan di: {json_path}")
        print("💡 Pastikan file 'result.json' hasil export Telegram sudah diletakkan di folder ini.")
        return False

    print(f"📖 Membaca file: {json_path} ...")
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    chat_name = data.get("name", "Telegram Chat")
    messages = data.get("messages", [])
    print(f"💬 Ditemukan total {len(messages)} pesan di chat '{chat_name}'")

    rows = []
    for msg in messages:
        # Hanya proses pesan biasa
        if msg.get("type") != "message":
            continue

        raw_text = extract_text_from_telegram_field(msg.get("text", ""))
        if not raw_text.strip():
            continue

        # Ekstraksi field jika formatnya adalah notifikasi bot EWS / Alert terstruktur
        time_match = re.search(r"Waktu\s*:\s*([^\n]+)", raw_text, re.IGNORECASE)
        status_match = re.search(r"Status\s*Tarikan\s*:\s*([^\n]+)", raw_text, re.IGNORECASE)
        total_match = re.search(r"Total\s*Database\s*:\s*([^\n]+)", raw_text, re.IGNORECASE)
        risk_match = re.search(r"Level\s*Risiko(?:\s*EWS)?\s*:\s*([^\n]+)", raw_text, re.IGNORECASE)
        keywords_match = re.search(r"Kata\s*Kunci\s*Top\s*:\s*([^\n]+)", raw_text, re.IGNORECASE)
        action_match = re.search(r"Rekomendasi\s*:\s*([^\n]+)", raw_text, re.IGNORECASE)

        # Baris pertama notifikasi biasanya judul/tipe alert
        lines = [line.strip() for line in raw_text.split("\n") if line.strip()]
        header_title = lines[0] if lines else ""

        rows.append({
            "id_pesan": msg.get("id"),
            "tanggal": msg.get("date"),
            "pengirim": msg.get("from", "Bot"),
            "judul_notif": header_title,
            "waktu_notif": time_match.group(1).strip() if time_match else "",
            "status_tarikan": status_match.group(1).strip() if status_match else "",
            "total_database": total_match.group(1).strip() if total_match else "",
            "level_risiko": risk_match.group(1).strip() if risk_match else "",
            "kata_kunci": keywords_match.group(1).strip() if keywords_match else "",
            "rekomendasi": action_match.group(1).strip() if action_match else "",
            "pesan_lengkap": raw_text
        })

    df = pd.DataFrame(rows)
    # Simpan dengan format UTF-8-SIG agar emoji dan karakter khusus terbaca rapi di Microsoft Excel
    df.to_csv(output_csv, index=False, encoding="utf-8-sig")

    print("\n" + "="*50)
    print(f"🎉 SUKSES! {len(df)} data berhasil dikonversi ke CSV.")
    print(f"📁 Lokasi output: {os.path.abspath(output_csv)}")
    print("="*50)
    return True

if __name__ == "__main__":
    # Cek apakah ada argumen path file atau default ke result.json
    target_file = sys.argv[1] if len(sys.argv) > 1 else "result.json"
    parse_telegram_json(target_file)

