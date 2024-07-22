#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]) {
    if (argc != 5) {
        printf("Usage: %s <name> <age> <email> <filename>\n", argv[0]);
        return 1;
    }

    char name[100];
    int age;
    char email[100];
    char filename[100];
    FILE *file;

    strcpy(name, argv[1]);
    age = atoi(argv[2]);
    strcpy(email, argv[3]);
    strcpy(filename, argv[4]);

    file = fopen(filename, "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    fprintf(file, "Name: %s\n", name);
    fprintf(file, "Age: %d\n", age);
    fprintf(file, "Email: %s\n", email);

    fclose(file);

    printf("\n--- Form Details ---\n");
    printf("Name: %s\n", name);
    printf("Age: %d\n", age);
    printf("Email: %s\n", email);
    printf("\nData has been saved to %s\n", filename);

    return 0;
}
