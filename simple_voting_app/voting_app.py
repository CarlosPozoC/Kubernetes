class VotingApp:
    def __init__(self):
        self.candidates = {}
        self.voters = set()

    def add_candidate(self, candidate_name):
        if candidate_name in self.candidates:
            print(f"{candidate_name} is already a candidate.")
        else:
            self.candidates[candidate_name] = 0
            print(f"{candidate_name} added successfully.")

    def cast_vote(self, voter_id, candidate_name):
        if voter_id in self.voters:
            print("You have already voted!")
        elif candidate_name not in self.candidates:
            print(f"{candidate_name} is not a valid candidate.")
        else:
            self.candidates[candidate_name] += 1
            self.voters.add(voter_id)
            print(f"Vote cast successfully for {candidate_name}.")

    def show_results(self):
        if not self.candidates:
            print("No candidates to display.")
            return

        print("\n--- Voting Results ---")
        for candidate, votes in self.candidates.items():
            print(f"{candidate}: {votes} votes")
        winner = max(self.candidates, key=self.candidates.get, default=None)
        print(f"\nWinner: {winner}" if winner else "\nNo votes cast yet.")

def main():
    app = VotingApp()
    while True:
        print("\n--- Voting App Menu ---")
        print("1. Add Candidate")
        print("2. Cast Vote")
        print("3. Show Results")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            candidate_name = input("Enter candidate name: ")
            app.add_candidate(candidate_name)
        elif choice == "2":
            voter_id = input("Enter your voter ID: ")
            candidate_name = input("Enter candidate name: ")
            app.cast_vote(voter_id, candidate_name)
        elif choice == "3":
            app.show_results()
        elif choice == "4":
            print("Exiting the app. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
