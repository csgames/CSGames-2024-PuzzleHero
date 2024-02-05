#include <iostream>
#include <string>
#include <map>
#include <algorithm>

const std::string choices[3] = {"rock", "paper", "scissors"};
const std::map<std::string, std::string> computer_choices = {
    {"rock", "paper"}, {"paper", "scissors"}, {"scissors", "rock"}
};

bool is_valid_choice(const std::string& choice) {
  for (const std::string& valid_choice : choices)
    if (choice == valid_choice)
      return true;

  return false;
}

std::string get_user_choice() {
  std::string choice;
  do {
    std::cout << "Choose rock, paper, or scissors: ";
    std::cin >> choice;
    std::transform(choice.begin(), choice.end(), choice.begin(), ::tolower);
  } while (!is_valid_choice(choice));
  return choice;
}

void play_rock_paper_scissors() {
  std::cout << "Welcome to Rock Paper Scissors!" << std::endl;

  std::string user_choice = get_user_choice();
  std::cout << "You chose " << user_choice << std::endl;

  std::string computer_choice = computer_choices.at(user_choice);
  std::cout << "The computer chose " << computer_choice << std::endl;
  std::cout << "You lose!" << std::endl;
}

bool ask_replay() {
  std::string play_again;
  std::cout << "Would you like to play again? (yes/no): ";
  std::cin >> play_again;
  std::transform(play_again.begin(), play_again.end(), play_again.begin(), ::tolower);

  return play_again == "yes" || play_again == "y" || play_again.empty();
}

void terminal() {
  while (true) {
    std::cout << ">";
    std::string input;
    std::cin >> input;

    if (input == "exit")
      break;

    if (input == "rps")
      do {
        play_rock_paper_scissors();
      } while (ask_replay());
  }
}

int main() {
    terminal();
    return 0;
}
