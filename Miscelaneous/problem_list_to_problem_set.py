def convertToSections(problem_list: str):
    for p in problem_list.split(', '):
        print("\\section{Problem " + p + "}\n\n    \\subsection{Solution}\n\n\\pagebreak")

if __name__ == "__main__":
    convertToSections('1, 3, 5, 7, 9, 11, 13, 17, 19, 23, 25, 27, 31, 35, 37, 39, 43, 45, 47, 51, 55, 57, 59, 63, 69, 75, 77')