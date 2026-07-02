from dataclasses import dataclass

@dataclass
class Entry:
    id: int
    date: str
    text: str

def main() -> None:
    id = 0
    while True:
        date = input("Enter date (MM/DD/YYYY): ")
        entry = input("Enter thoughts for the day: ")
        entry = Entry(id=id, date=date, text=entry)
        print(f"{date}: {entry}")
        id += 1

if __name__ == "__main__":
    main()
