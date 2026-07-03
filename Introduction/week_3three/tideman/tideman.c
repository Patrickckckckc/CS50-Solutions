#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// preferences[i][j] is number of voters who prefer i over j
int preferences[MAX][MAX];

// locked[i][j] means i is locked in over j
bool locked[MAX][MAX];

// Each pair has a winner, loser
typedef struct
{
    int winner;
    int loser;
} pair;

// Array of candidates
string candidates[MAX];
bool candidates_winners[MAX] = {true};
pair pairs[MAX * (MAX - 1) / 2];

int pair_count;
int candidate_count;

// Function prototypes
bool vote(int rank, string name, int ranks[]);
void record_preferences(int ranks[]);
void add_pairs(void);
void sort_pairs(void);
void lock_pairs(void);
void print_winner(void);
bool cycle(int i);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: tideman [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i] = argv[i + 1];
    }

    // Clear graph of locked in pairs
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            locked[i][j] = false;
        }
    }

    pair_count = 0;
    int voter_count = get_int("Number of voters: ");

    // Query for votes
    for (int i = 0; i < voter_count; i++)
    {
        // ranks[i] is voter's ith preference
        int ranks[candidate_count];

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Rank %i: ", j + 1);

            if (!vote(j, name, ranks))
            {
                printf("Invalid vote.\n");
                return 3;
            }
        }

        record_preferences(ranks);

        printf("\n");
    }

    add_pairs();
    sort_pairs();
    for (int i = 0; i < pair_count; i++)
    {
        printf("Pair %i: winner=%i, loser=%i\n", i, pairs[i].winner, pairs[i].loser);
    }

    lock_pairs();
    print_winner();
    return 0;
}

// Update ranks given a new vote
bool vote(int rank, string name, int ranks[])
{
    // TODO
    for (int i = 0; i < candidate_count; i++)
    {
        if (strcmp(name, candidates[i]) == 0)
        {
            // UPDATE
            ranks[rank] = i;
            return true;
        }
    }
    return false;
}

// Update preferences given one voter's ranks
void record_preferences(int ranks[])
{
    // TODO
    int n = 0;
    do
    {
        for (int x = n + 1; x < candidate_count; x++)
        {
            preferences[ranks[n]][ranks[x]] += 1;
        }
        n++;
    }
    while (n != candidate_count - 1);
    return;
}

// Record pairs of candidates where one is preferred over the other
void add_pairs(void)
{
    // TODO
    // Check for each pair [i][j]  and [j][i], just is something is greather than the other counts
    // Update the pair array
    int i = 0;
    int index_pair = 0;
    do
    {
        for (int j = 0; j < candidate_count; j++)
        {
            if (preferences[i][j] > preferences[j][i])
            {
                // Update pair array
                pairs[index_pair].winner = i;
                pairs[index_pair].loser = j;
                index_pair++;
                // Update Global Variable
                pair_count++;
            }
        }
        i++;
    }
    while (i != candidate_count);

    return;
}

// Sort pairs in decreasing order by strength of victory
void sort_pairs(void)
{
    // TODO
    // Iterate in the PAIR ARRAY
    for (int i = 0; i < pair_count; i++)
    {
        int biggest_number = 0;
        int index_biggest_number = 0;
        // Checking BIGGEST NUMBER
        for (int j = i; j < pair_count; j++)
        {
            if (preferences[pairs[j].winner][pairs[j].loser] -
                    preferences[pairs[j].loser][pairs[j].winner] >
                biggest_number)
            {
                biggest_number = preferences[pairs[j].winner][pairs[j].loser] -
                                 preferences[pairs[j].loser][pairs[j].winner];
                index_biggest_number = j;
            }
        }

        // Making a SWAP BETWEEN BIGGEST NUMBER
        pair swap_holder[1];
        swap_holder[0] = pairs[index_biggest_number];
        pairs[index_biggest_number] = pairs[i];
        pairs[i] = swap_holder[0];
    }
    return;
}

// Lock pairs into the candidate graph in order, without creating cycles
void lock_pairs(void)
{
    // TODO
    // Iterate for Each Pair
    for (int i = 0; i < pair_count; i++)
    {
        // Checking Just False Values
        if (locked[pairs[i].winner][pairs[i].loser] == false)
        {
            locked[pairs[i].winner][pairs[i].loser] = true;
            // Check if creates a cycle change to false
            if (cycle(i))
            {
                candidates_winners[i] = true;
                locked[pairs[i].winner][pairs[i].loser] = false;
                continue;
            }
        }
    }
    return;
}

bool cycle(int i)
{
    // base case is index 0
    if (i == 0)
    {
        int index = pairs[i].loser;
        candidates_winners[index] = false;
        return false;
    }

    // Recursive case
    if (!cycle(i - 1))
    {
        int index = pairs[i].loser;
        candidates_winners[index] = false;
    }

    // Looking for possible winners, if they are not IS A CYCLE
    for (int j = 0; j < candidate_count; j++)
    {
        if (candidates_winners[i] == true)
        {
            return false;
        }
    }
    return true;
}

// Print the winner of the election
void print_winner(void)
{
    // TODO
    for (int j = 0; j < candidate_count; j++)
    {
        if (candidates_winners[j] == true)
        {
            printf("The winner is %s\n", candidates[j]);
        }
    }
    return;
}
