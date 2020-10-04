
var p1 = new Point(1,2);
var p2 = Point.random();
var p3 = new Point(-5, 2);
var p4 = Point.random();
var p5 = p1.add(p2);


var s1 = new Segment(p1, p2);
var s2 = Segment.random();
var s3 = s1.add(s2);

var pl1 = new Polygon(p1, p2, p3);
var pl2 = pl1.neg();
