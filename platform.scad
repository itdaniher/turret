$fn=100;


d = 4.78;
r1 = d/2;
r2 = 10;

t = 4;

c1 = 36.16;
c2 = 68.60;

motorshaft = 3.96;
flatside = 3.42;

offset = 10;

difference() {
translate(v = [-offset/2, -offset/2]) cube(size = [c2+offset, c1+offset, t]);

translate(v = [0, 0]) cylinder(r = r1, h = t);
translate(v = [0, c1]) cylinder(r = r1, h = t);
translate(v = [c2, 0]) cylinder(r = r1, h = t);
translate(v = [c2, c1]) cylinder(r = r1, h = t);

translate(v = [c2/2, c1/2]) difference() {
cylinder(r=motorshaft/2, h = t);
translate(v = [-flatside/2, flatside/2]) cube(flatside);
}
}
projection(cut = true);