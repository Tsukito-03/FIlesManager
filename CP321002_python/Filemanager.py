from pathlib import Path
import shutil


def Files_Organize (target_directory):
  target_path = Path(target_directory)
  directory_map= {"Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
"Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".csv"],
"Videos": [".mp4", ".mkv", ".avi", ".mov", ".flv"],
"Music": [".mp3", ".wav", ".aac", ".flac"],
"Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
"Programs": [".exe", ".msi", ".dmg", ".pkg"]}

  if not target_path.exists():
    print(f"ไม่พบโฟลเดอร์: {target_path}")
    return

  print(f"กำลังจัดระเบียบไฟล์ใน: {target_path}")

  for item in target_path.iterdir():
    if item.is_file():
      file_extension = item.suffix.lower()
      moved = False

      for category, extensions in directory_map.items():
        if file_extension in extensions:
          category_path = target_path / category
          category_path.mkdir(exist_ok=True)

          destination = category_path / item.name

          if destination.exists():
            counter = 1
            while True:
              new_name = f"{item.stem}_{counter}{item.suffix}"
              destination = category_path / new_name
              if not destination.exists():
                break
              counter += 1

          shutil.move(str(item), str(destination))
          print(f"ย้าย: {item.name} -> {category}/")
          moved = True
          break

      if not moved:
        others_path = target_path / "Others"
        others_path.mkdir(exist_ok=True)
        destination = others_path / item.name

        if destination.exists():
          counter = 1
          while True:
            new_name = f"{item.stem}_{counter}{item.suffix}"
            destination = others_path / new_name
            if not destination.exists():
              break
            counter += 1

        shutil.move(str(item), str(destination))
        print(f"ย้าย: {item.name} -> Others/")

  print("จัดระเบียบไฟล์เสร็จสิ้นเรียบร้อยแล้ว!")

if __name__ == "__main__":
  keyinp=input('Enter directory ')
  path_to_organize = Path.home() / keyinp
  Files_Organize(path_to_organize)
  