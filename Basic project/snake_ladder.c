// SNAKE LADDEER Code

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
void snake(char user[20], int *p)
{
    // int total;
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
    unsigned int j = 1;
    for (int i = 1; i <= 10; i++)
    {
        for (j; j <= 10 * i; j++)
        {
            if (point == j)
            {
                printf(" %s ", user);
                continue;
            }
            printf(" %d ", j);
        }
        for (j; j <= 10 * i; j++)
        {
            printf(" %d ", j);
        }
        printf("\n");
    }
}
int main()
{
    int point1 = 0, point2 = 0;
    char user1[20] = {20};
    printf("\nEnter your name user1: ");
    scanf("%s", &user1);
    getchar();
    char user2[20] = {20};
    printf("\nEnter your name user2: ");
    scanf("%s", &user2);
    getchar();

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
    return 0;
}
