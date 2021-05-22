#include <cstdio>
#include <cstdint>

typedef int point_t;


union ipv4 {
	uint32_t i32;
	struct {
		point_t a;
		uint8_t b;
		uint8_t c;
		uint8_t d;
	} octets;
};

int main_union() {
	union ipv4 addr;
	addr.octets = {192, 168, 0, 105};
	printf("ip address is %d.%d.%d.%d\n %d", addr.octets.a, addr.octets.b, addr.octets.c, addr.octets.d, addr.i32);

	return 0;
}