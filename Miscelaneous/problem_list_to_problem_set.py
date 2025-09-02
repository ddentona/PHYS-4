def convertToSections(problem_list: str):
    for p in problem_list.split(', '):
        print("\\section{Problem " + p + "}\n\n    \\subsection{Solution}\n\n\\pagebreak")

if __name__ == "__main__":
    convertToSections('1, 3, 5, 7, 9, 15, 23, 25, 27, 29, 37, 39, 43, 45, 49, 53, 57, 67, 71')