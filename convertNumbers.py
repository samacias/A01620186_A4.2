import sys
import time

HEX_DIGITS = "0123456789ABCDEF"


def reverse_text(text: str) -> str:
    reversed_text = ""
    i = len(text) - 1
    while i >= 0:
        reversed_text += text[i]
        i -= 1
    return reversed_text


def to_binary(number: int) -> str:
    if number == 0:
        return "0"

    sign = ""
    n = number
    if n < 0:
        sign = "-"
        n = -n

    bits = ""
    while n > 0:
        remainder = n % 2
        if remainder == 0:
            bits += "0"
        else:
            bits += "1"
        n //= 2

    return sign + reverse_text(bits)


def to_hexadecimal(number: int) -> str:
    if number == 0:
        return "0"

    sign = ""
    n = number
    if n < 0:
        sign = "-"
        n = -n

    digits = ""
    while n > 0:
        remainder = n % 16
        digits += HEX_DIGITS[remainder]
        n //= 16

    return sign + reverse_text(digits)


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python convertNumbers.py fileWithData.txt")
        return

    start = time.time()
    filename = sys.argv[1]

    lines_output = []
    lines_output.append("Number | Binary | Hexadecimal")
    lines_output.append("------------------------------------------")

    invalid_lines = 0
    valid_numbers = 0

    with open(filename, "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            raw = line.strip()

            if raw == "":
                invalid_lines += 1
                print(f"Invalid data (empty) at line {line_number} -> skipped")
                continue

            try:
                if "." in raw:
                    raise ValueError("float not allowed for this exercise")
                number = int(raw)
                valid_numbers += 1

                binary_value = to_binary(number)
                hex_value = to_hexadecimal(number)

                lines_output.append(f"{number} | {binary_value} | {hex_value}")

            except ValueError:
                invalid_lines += 1
                print(f"Invalid data '{raw}' at line {line_number} -> skipped")

    elapsed = time.time() - start
    lines_output.append("")
    lines_output.append(f"Valid numbers: {valid_numbers}")
    lines_output.append(f"Invalid lines: {invalid_lines}")
    lines_output.append(f"Time: {elapsed:.6f} seconds")

    result_text = "\n".join(lines_output)

    print(result_text)

    with open("ConvertionResults.txt", "w", encoding="utf-8") as out:
        out.write(result_text)
        out.write("\n")


if __name__ == "__main__":
    main()