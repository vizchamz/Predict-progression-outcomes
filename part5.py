# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.

# Student ID: UOW - w1811026 , IIT 20201217

# Date:  2020 / 12 / 11

data = [[120, 0, 0], [100, 20, 20], [100, 0, 20], [80, 20, 20], [60, 40, 20],
        [40, 40, 40], [20, 40, 60], [20, 20, 80], [20, 0, 100], [0, 0, 120]]

progress = []
trailer = []
retriever = []
exclude = []

pass_credits = 0
defer_credits = 0
fail_credits = 0


def progress_outcome():
    if pass_credits == 120:
        print("Progress")
        progress.append(0)
    elif pass_credits == 100 and defer_credits == 20:
        print("Progress (module trailer)")
        trailer.append(0)
    elif fail_credits == 20 and pass_credits == 100:
        print("Progress (module trailer)")
        trailer.append(0)
    elif pass_credits == 80 and defer_credits == 20:
        print("Do not Progress - module retriever")
        retriever.append(0)
    elif pass_credits == 60 and defer_credits == 40:
        print("Do not Progress - module retriever")
        retriever.append(0)
    elif pass_credits == 40 and defer_credits == 40:
        print("Do not Progress - module retriever")
        retriever.append(0)
    elif pass_credits == 20 and defer_credits == 40:
        print("Do not Progress - module retriever")
        retriever.append(0)
    elif fail_credits == 80 and pass_credits == 20:
        print("Exclude")
        exclude.append(0)
    elif pass_credits == 20 and fail_credits == 100:
        print("Exclude")
        exclude.append(0)
    elif fail_credits == 120:
        print("Exclude")
        exclude.append(0)


def validation(data):
    global pass_credits, defer_credits, fail_credits
    for i in range(len(data)):
        pass_credits = data[i][0]
        defer_credits = data[i][1]
        fail_credits = data[i][2]
        progress_outcome()


def histogram_print():
    print("\n")
    print("-" * 60)
    print("Horizontal Histogram\n")
    print("Progress", "", len(progress), ":", "*" * len(progress))
    print("Trailer", " ", len(trailer), ":", "*" * len(trailer))
    print("Retriever", len(retriever), ":", "*" * len(retriever))
    print("Excluded", "", len(exclude), ":", "*" * len(exclude))
    total_outcomes = len(progress) + len(trailer) + len(retriever) + len(exclude)
    print("\n")
    print(total_outcomes, "outcomes in total.")
    progress.clear()
    trailer.clear()
    retriever.clear()
    exclude.clear()
