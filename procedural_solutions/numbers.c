#include <stdio.h>
#include <math.h>
#include <ctype.h>

void clear_input_buffer() {
	int c;
	while ((c = getchar()) != '\n' && c != EOF);
}

// ================== ================== ==================
double find_pi_to_nth_digit(int n), find_e_to_nth_digit(int n), tile_cost(double w, double h, double c);
void fibonacci_to_n(int n), n_fibonacci_elements(int n), prime_factors(int n), find_next_prime();
int is_prime(int n);

// ****************** ****************** ******************
int main() {
	unsigned n;
	// Find pi to nth digit
	printf("Enter the number of decimal places: ");
	if (scanf_s("%u", &n) != 1 || ferror(stdin) || n>100 ) {
		printf("Invalid input\n");
		clear_input_buffer();
		return 1;
	}
	double pi = find_pi_to_nth_digit(n);
	printf("Pi = %.*f\n", n, pi);

	// Find E to nth digit
	printf("Enter the number of decimal places: ");
	if (scanf_s("%u", &n) != 1 || ferror(stdin) || n > 100) {
		printf("Invalid input\n");
		clear_input_buffer();
		return 1;
	}
	double e = find_e_to_nth_digit(n);
	printf("E = %.*f\n", n, e);

	// Print fibonacci sequence up to n
	printf("Enter the limt: ");
	if (scanf_s("%u", &n) != 1 || ferror(stdin)) {
		printf("Invalid input\n");
		clear_input_buffer();
		return 1;
	}
	fibonacci_to_n(n);

	// Print n fibonacci sequence elements
	printf("Enter the number of elements: ");
	if (scanf_s("%u", &n) != 1 || ferror(stdin)) {
		printf("Invalid input\n");
		clear_input_buffer();
		return 1;
	}
	n_fibonacci_elements(n);

	// Find all prime factors
	printf("Enter a number greater than 2: ");
	if (scanf_s("%u", &n) != 1 || ferror(stdin) || n < 2) {
		printf("Invalid input\n");
		clear_input_buffer();
		return 1;
	}
	prime_factors(n);

	// Find prime numbers until the user chooses to stop asking for the next one
	find_next_prime();

	// Find Cost of Tile to Cover W x H Floor
	double w, h, c;
	printf("Enter width, height and cost: ");
	if (scanf_s("%lf %lf %lf", &w, &h, &c) != 3 || ferror(stdin)) {
		printf("Wrong input");
		clear_input_buffer();
		return 1;
	}
	if (w < 0 || h < 0 || c < 0) {
		printf("All numbers must be positive\n");
		return 1;
	}
	printf("Tile cost: %.2f$\n", tile_cost(w, h, c));

}

// ================== ================== ==================
double find_pi_to_nth_digit(int n) {
	double accuracy = pow(10, -n);
	double a = 1.0;
	double b = 1.0 / pow(2, 0.5);
	double t = 0.25;
	double p = 1.0;

	while (fabs(a - b) > accuracy) {
		double a_next = (a + b) / 2;
		b = pow((a * b), 0.5);
		t -= p * (pow(a - a_next, 2));
		a = a_next;
		p *= 2;
	}

	double pi = (pow(a + b, 2) / (4 * t));
	double factor = pow(10, n);
	pi = round(pi * factor) / factor;

	return pi;

}

double find_e_to_nth_digit(int n)
{
	double accuracy = pow(10, -n);
	double e = 0.0;
	double factorial = 1.0;
	double k = 0.0;

	while (1) {
		e += (1.0 / factorial);
		if ((1.0 / factorial) < accuracy) {
			break;
		}
		k += 1;
		factorial *= k;
	}
	double factor = pow(10, n);
	e = round(e * factor) / factor;
	return e;
}

void fibonacci_to_n(int n) {
	printf("Fibonacci sequence: ");

	if (n >= 0) printf("0 ");
	if (n >= 1) printf("1 ");

	int f1 = 0, f2 = 1;
	while (1) {
		int next = f1 + f2;
		if (next > n) {
			break;
		}
		printf("%d ", next);
		f1 = f2;
		f2 = next;
	}
	printf("\n");
}

void n_fibonacci_elements(int n) {
	printf("Fibonacci sequence: ");
	if (n >= 1) printf("0 ");
	if (n >= 2) printf("1 ");

	unsigned f1 = 0, f2 = 1;
	for (int i = 2; i < n; i++) {
		unsigned next = f1 + f2;
		printf("%u ", next);
		f1 = f2;
		f2 = next;
	}
	printf("\n");
}

void prime_factors(int n) {
	printf("Prime factors: ");
	while (n % 2 == 0) {
		printf("2 ");
		n /= 2;
	}
	int limit = pow(n, 0.5) + 1;
	for (int i = 3; i < limit; i += 2) {
		while (n % i == 0) {
			printf("%d ", i);
			n /= i;
		}
	}
	if (n > 2) {
		printf("%d", n);
	}
	printf("\n");
}

int is_prime(int n) {
	if (n <= 1) return 0;
	if (n == 2) return 1;
	if (n % 2 == 0) return 0;

	for (int i = 3; i * i <= n; i+=2) {
		if (n % i == 0) return 0;
	}
	return 1;
}

void find_next_prime() {
	int current = 2;
	char choice;
	printf("Press 'n' for next prime, any other key to quit\n");
	
	while (1) {
		if (is_prime(current)) {
			printf("%d is prime, continue? ", current);
			if (scanf_s("%c", &choice,1) != 1 || ferror(stdin) || (tolower(choice) != 'n')) {
				clear_input_buffer();
				break;
			}
			clear_input_buffer();
		}
		current++;
	}
	printf("\nPrime number generation stopped\n");
}

double tile_cost(double w, double h, double c) {
	return(w * h * c);
}
