

### Loudspeaker Problem

#### Problem Description:
You are given `A` cities and a road network represented by an array `B` of size `M * 2`. Each element `B[i][0]` and `B[i][1]` indicates that there is a road connecting cities `B[i][0]` and `B[i][1]`.

There is also an array `C` which lists the cities equipped with loudspeakers. A loudspeaker can transmit its sound across cities through roads. Each loudspeaker has a uniform intensity level `x`, which determines how far the sound can travel: it reaches all cities within a distance of `x` from the source city (in terms of road distance).

A loudspeaker will automatically turn on if it receives sound from another loudspeaker. You are tasked with finding the minimum intensity `x` such that the sound initiated manually at a city `D` can reach a destination city `E`.

If it's impossible to transmit sound from city `D` to city `E`, return `-1`.

#### Input Format:
- First argument is an integer `A`, representing the number of cities.
- Array `B`, where each element `B[i][0]` and `B[i][1]` represents a road between two cities.
- Array `C`, listing the cities equipped with loudspeakers.
- Two integers, `D` and `E`, representing the source city and the destination city, respectively.

#### Output Format:
Return the minimum loudspeaker intensity `x` required for sound to propagate from city `D` to city `E`. If it's impossible, return `-1`.

#### Constraints:
- `1 <= A <= 10^5`
- `0 <= |B| <= 10^5`
- `1 <= B[i][0], B[i][1] <= A`
- `B[i][0] != B[i][1]`
- `1 <= |C| <= 10^5`
- `1 <= C[i] <= A`
- `1 <= D, E <= A`




to check: 

https://www.youtube.com/watch?v=B_W0NO9wQKY&t=1446s


