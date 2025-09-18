def convertToSections(problem_list: str):
    for p in problem_list.split(', '):
        print("\\section{Problem " + p + "}\n\n    \\subsection{Solution}\n\n\\pagebreak")

if __name__ == "__main__":
    convertToSections('1, 5, 9, 13, 15, 19, 21, 37, 39, 45, 47, 49, 59, 63, 65, 69, 75, 77, 93')
