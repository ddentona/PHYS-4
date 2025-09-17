def convertToSections(problem_list: str):
    for p in problem_list.split(', '):
        print("\\section{Problem " + p + "}\n\n    \\subsection{Solution}\n\n\\pagebreak")

if __name__ == "__main__":
    convertToSections('1, 3, 5, 9, 15, 19, 21, 25, 30, 31, 35, 37, 41, 43, 45, 53, 61, 65, 73, 75, 83')
