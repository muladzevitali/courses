#include <iostream>
#include <ctime>

using namespace std;

const int MAX_CHIPS = 100;
const float MAX_TURN = .5;

int main() {
    bool player_1_turn = true;
    bool game_over = false;
    unsigned short int current_player_index = 0;

    int chips_taken = 0;

    string player_names[2];

    cout << "Player 1 type your name: ";
    cin >> player_names[0];
    cout << "Player 2 type your name: ";
    cin >> player_names[1];

    srand(time(0));

    int chips_in_pile = rand() % MAX_CHIPS + 1;
    cout << "This round will start with " << chips_in_pile << " chips in pile\n";
    while (!game_over) {
        const int MAX_PER_TURN = chips_in_pile * MAX_TURN;
        do {
            if (player_1_turn) {
                current_player_index = 0;
            } else {
                current_player_index = 1;
            }
            cout << "You can only take up to ";
            if (MAX_PER_TURN == 0) {
                cout << "1\n";
            } else {
                cout << MAX_PER_TURN << " chips\n";
            }
            cout << player_names[current_player_index] << " how many chips would you like? ";
            cin >> chips_taken;
            cout << "Chips taken " << chips_taken << endl;
        } while ((chips_taken > MAX_PER_TURN) and (chips_taken > 1));
        chips_in_pile -= chips_taken;
        cout << "Chips left " << chips_in_pile << endl;
        if (chips_in_pile == 0) {
            game_over = true;
            cout << player_names[current_player_index] << ", congratulations you won!";
        } else {
            player_1_turn = !player_1_turn;
        }
    }


}