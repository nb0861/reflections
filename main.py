from dataclasses import dataclass

@dataclass
class Entry:
    id: int
    date: str
    text: str

def main() -> None:
    id = 0
    while True:
        date = input("Enter date (MM/DD/YYYY, or press Enter to finish): ").strip()
        if not date or date.lower() in {"quit", "q", "done"}:
            break

        text = input("Enter thoughts for the day: ")
        entry = Entry(id=id, date=date, text=text)
        print(f"{date}: {entry}")
        id += 1

if __name__ == "__main__":
    main()
