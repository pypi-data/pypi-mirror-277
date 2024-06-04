# API

Due to the computationally resource-intensive nature of calculating the Foo et al. parameterization, we are currently developing API endpoints that will allow users to run the Foo (Et Al)^2 package on NSF supercomputer clusters. To join the waitlist, please email [josephwillemricci@gmail.com](), or join the [discussion forum](https://groups.google.com/g/foo_et_al_2).


`foo_et_al.foo_et_al.foo_et_al_param(radius)`:

Calculates the volume of a sphere using the complex Foo et al. parameterization. This function serves as an interface to the more general volume calculation provided by vol_sphere.

Parameters:
radius (float or int): The radius of the sphere. Must be a non-negative value.

Returns:
float: The volume of the sphere calculated using the formula (4/3) * pi * radius^3.

Raises:
ValueError: If the radius is negative or None

Examples:
`>>> foo_et_al_param(1)`

`4.1887902047863905`

Note:
This implementation assumes the radius is in the same unit as the desired volume output.

`foo_et_al.utils.vol_sphere(radius)`:

Calculates the volume of a sphere given its radius using the mathematical formula V = (4/3) * π * r^3.

Parameters:
radius (float): The radius of the sphere. Radius must be a non-negative number.

Returns:
float: The volume of the sphere calculated using the specified radius.

Raises:
ValueError: If 'radius' is None or a negative number.

Examples:
`>>> vol_sphere(1)`

`4.1887902047863905`