"""

Question:
implement a program that prompts the user for the name of a file and then
outputs that file’s media type if the file’s name ends, case-insensitively,
in any of these suffixes:
.gif, .jpg,.jpeg,.png, .pdf, .txt, .zip
"""


def get_extension(filename: str) -> str:
    index = filename.rfind(".")
    if index == -1:
        return ""
    return filename[index + 1 :].lower()


def get_media_type(extension: str) -> str:
    match extension:
        case "gif":
            return "image/gif"
        case "jpg" | "jpeg":
            return "image/jpeg"
        case "png":
            return "image/png"
        case "pdf":
            return "application/pdf"
        case "txt":
            return "text/plain"
        case "zip":
            return "application/zip"
        case _:
            return "application/octet-stream"

    # types = {
    #     "gif": "image/gif",
    #     "jpg": "image/jpeg",
    #     "jpeg": "image/jpeg",
    #     "png": "image/png",
    #     "pdf": "application/pdf",
    #     "txt": "text/plain",
    #     "zip": "application/zip",
    # }
    # return types.get(extension, "application/octet-stream")


def main():
    filename = input("File name: ").rstrip()
    extension = get_extension(filename)
    media_type = get_media_type(extension)
    print(f"Media type: {media_type}")


main()
