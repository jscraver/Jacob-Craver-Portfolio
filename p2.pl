/*
NAME(S): Jacob Craver
DATE: 02/20/22
COURSE: 330-001
QUARTER: Winter
PROJECT: 2
*/

/*Finds the distance between two points*/
dist((X1,Y1,Z1),(X2,Y2,Z2),R) :- R is sqrt((X2-X1)**2+(Y2-Y1)**2+(Z2-Z1)**2).

/*Finds the length of a vector*/
vecLength((X,Y,Z),R) :- R is sqrt(X**2+Y**2+Z**2).

/*Finds the length of the normal vector (length 1) using the vector length formula above*/
vecNorm((X,Y,Z),R) :- vecLength((X,Y,Z),D), X1 is X/D, Y1 is Y/D, Z1 is Z/D, R = vec(X1,Y1,Z1).

/*Finds the dot product of two vectors*/
vecDot((X1,Y1,Z1),(X2,Y2,Z2),R) :- R is X1*X2+Y1*Y2+Z1*Z2.

/*Finds the angle between two vectors using the dot product and vector length formulas above*/
vecAngle((X1,Y1,Z1),(X2,Y2,Z2),R) :- vecDot((X1,Y1,Z1),(X2,Y2,Z2),N), vecLength((X1,Y1,Z1),D1), vecLength((X2,Y2,Z2),D2), R is acos(N/(D1*D2)).

/*Checks if two vectors are orthagonal using the dot product formula above*/
areOrthog((X1,Y1,Z1),(X2,Y2,Z2)) :- vecDot((X1,Y1,Z1),(X2,Y2,Z2),R), R = 0.

/*Finds the cross product of two vectors*/
vecCross((X1,Y1,Z1),(X2,Y2,Z2),R) :- I is Y1*Z2-Y2*Z1, J is -(X1*Z2-X2*Z1), K is X1*Y2-X2*Y1, R = (I,J,K).

/*Finds the vector projection of the first vector onto the second vector*/
vecProj((X1,Y1,Z1),(X2,Y2,Z2),R) :- vecDot((X1,Y1,Z1),(X2,Y2,Z2),N), vecLength((X2,Y2,Z2),D), S is N/D**2, I is S*X2, J is S*Y2, K is S*Z2, R = (I,J,K).

/*Finds the shortest distance bewteen a point and a line using the vector projection and distance formulas above*/
distPointLine((X1,Y1,Z1),(X2,Y2,Z2),(X3,Y3,Z3),R) :- X4 is X3-X1, Y4 is Y3-Y1, Z4 is Z3-Z1, vecProj((X4,Y4,Z4),(X2,Y2,Z2),N), dist((X4,Y4,Z4),N,F), R is F.

/*Finds the shortest distance between a point and a plane using the dot product and vector length formulas above*/
distPointPlane((X1,Y1,Z1),(X2,Y2,Z2),(X3,Y3,Z3),R) :- vecDot((X1,Y1,Z1),(X2,Y2,Z2),N), vecDot((X2,Y2,Z2),(X3,Y3,Z3),R1), I is -R1, vecLength((X2,Y2,Z2),D), R is (N+I)/D.