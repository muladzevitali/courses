#include <iostream>
#include <string>


class Rational {
	int n = 0;
	int d = 1;
public:
	Rational(int numerator = 0, int denominator = 1) :n(numerator), d(denominator) {};
	Rational(const Rational& r) :n(r.n), d(r.d) {};
	~Rational();

	int numerator() const { return n; }
	int denomerator() const { return d; }

	Rational reduce() const;
	std::string string() const;
	std::string raw_string() const;

	Rational& operator = (const Rational&);
	Rational operator - (const Rational&) const;
	Rational operator * (const Rational&) const;
	Rational operator / (const Rational&) const;
};

Rational& Rational::operator = (const Rational& other) {
	if (this != &other) {
		n = other.n;
		d = other.d;
	}

	return *this;
}

Rational Rational::reduce() const {
	if (n == 0 || d <= 3) return *this;
	for (int div = d / 2; div; --div) {
		if (n % div == 0 && d % div == 0) {
			return Rational(n / div, d / div);
		}
	}

	return *this;
}


std::string Rational::string() const{
	if (d == 0) return "[NAN]";
	if (d == 1 && n == 0) return std::to_string(n);

	int abs_n = abs(n);
	if (abs_n > d) {
		int whole = n / d;
		int remainder = abs_n % d;
		if (remainder) return std::to_string(whole) + ' ' + Rational(remainder, d).string();
		else return std::to_string(whole);
	}
	else {
		return reduce().raw_string();
	}
}

std::string Rational::raw_string() const {
	return std::to_string(n) + "/" + std::to_string(d);
}



Rational Rational::operator - (const Rational& r) const {
	return Rational(n * r.d - d * r.n, d * r.d);
}

Rational Rational::operator * (const Rational& r) const {
	return Rational(n * r.n, d * r.d);
}

Rational Rational::operator / (const Rational& r) const {
	return Rational(n * r.d, d * r.n);
}

Rational::~Rational() {
	n = 0;
	d = 1;
}

std::ostream& operator << (std::ostream& o, const Rational& r) {
	return o << r.raw_string();
}

Rational operator + (const Rational& l, const Rational& r)  {
	return Rational(l.numerator() * r.denomerator() + l.denomerator() * r.numerator(), l.denomerator() * r.denomerator());
}


int main_rational() {
	Rational a = 7;
	std::cout << "a is: " << a << std::endl;

	Rational b(25, 15);
	std::cout << "b is: " << b << std::endl;

	Rational c = b;
	std::cout << "c is: " << c << std::endl;

	Rational d;
	std::cout << "d is: " << d << std::endl;

	d = c;
	std::cout << "d is: " << d << std::endl;

	Rational& e = d;
	d = e;
	std::cout << "e is: " << e << std::endl;

	std::cout << std::endl;
	std::cout << d.string() << std::endl;
	std::cout << 14 + a << std::endl;

	std::cout << a + b << std::endl;
	return 0;

}