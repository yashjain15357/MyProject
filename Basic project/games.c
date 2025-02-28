// SNAKE LADDEER Code

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
void snake(char user[20], int *p)
{
    int point = *p;
    srand(time(NULL));
    int dice = rand() % 6 + 1;
    printf("%s it's your turn...\npress enter button for rolled dice \n", user);
    getchar(); // Wait for Enter key press
    printf("%s your dice is rolled....%d\n", user, dice);
    point = point + dice;
    switch (point)
    {
    case 4:
        point = 25;
        break;
    case 21:
        point = 39;
        break;
    case 29:
        point = 74;
        break;
    case 43:
        point = 76;
        break;
    case 63:
        point = 80;
        break;
    case 71:
        point = 89;
        break;
    case 30:
        point = 7;
        break;
    case 47:
        point = 15;
        break;
    case 56:
        point = 19;
        break;
    case 73:
        point = 51;
        break;
    case 82:
        point = 42;
        break;
    case 92:
        point = 75;
        break;
    case 98:
        point = 55;
        break;
    }
    if (point > 100)
    {
        point = point - dice;
    }
    printf("%s your present point is %d\n\n", user, point);

    *p = point;
}
char name[10];
int d, e, points = 0;
void rps() // rock paper scissor function
{
    char user[10];
    char a[] = "ROCK", b[] = "PAPER", c[] = "SCISSOR";

    printf("%s Type your option : \n1>> ROCK\n2>> PAPER\n3>> SCISSOR\n", name);

    scanf("%s", user);

    if (strcmp(user, "rock") == 0)
    {
        e = 0;
    }
    else if (strcmp(user, "paper") == 0)
    {
        e = 1;
    }
    else if (strcmp(user, "scissor") == 0)
    {
        e = 2;
    }
    // printf("e = %d\n", e);
    srand(time(NULL));
    d = rand() % 3;
    if (d == 0)
    {
        printf("%s\n", a);
    }
    if (d == 1)
    {
        printf("%s\n", b);
    }
    if (d == 2)
    {
        printf("%s\n", c);
    }
}
int main()
{
    printf("choose the game number \n");
    printf("1>> Rock Paper Scissor Game \n");
    printf("2>> Snake Ladder Game\n");
    int option;
    scanf("%d", &option);
    if (option == 1)
    {
        printf("enter your name\n");
        scanf("%s", &name);

        printf("now your game is start \n");
        printf("%s VS computer\n", name);

        for (int i = 0; i <= 3; i++)
        {
            rps();
            if (d == e)
            {
                points = points + 0;
            }
            if ((d == 0 && e == 1) || (d == 2 && e == 0) || (d == 1 && e == 2))
            {
                points++;
            }
            if ((d == 0 && e == 2) || (d == 2 && e == 1) || (d == 1 && e == 0))
            {
                points--;
            }
            printf("Your Total Points = %d\n", points);
            i = points;
        }
    }
    if (option == 2)
    {
        int point1 = 0, point2 = 0;
        char user1[20] ;
        printf("\nEnter your name user1: ");
        scanf("%s", &user1);
        char user2[20] ;
        printf("\nEnter your name user2: ");
        scanf("%s", &user2);

        for (int i = 1; i <= 100; i++)

        {

            snake(user1, &point1);

            snake(user2, &point2);
            // getchar(); // Wait for Enter key press
            if (point1 >= 100)
            {
                printf("Congrulation %s you win \n", user1);
                break;
            }
            if (point2 >= 100)
            {
                printf("Congrulation %s you win \n", user2);
                break;
            }
            if (point1 >= 100 && point2 >= 100)
            {
                printf("%s and %s  your match is tie \n", user1, user2);
                break;
            }
        }
    }

    return 0;
}
