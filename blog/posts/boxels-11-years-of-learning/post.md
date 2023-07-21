## Introduction

![Boxel Screenshot](../static/img/boxels-screenshot-3.png)

It's taken me a lot of personal development to get to the point where I could
even finish something I'd call a "game". Boxels is not that. Other than walking
around, there is nothing to iteract with in the gameworld. Instead, I would
consider this project to be an extensible base upon which to build more
functionality later. For instance, the barebones entity system can be extended
to support picking up items or adding vegetation to the world.

For the longest time I worked on "games" only to the point of seeing something
on screen or achieving a particular technical accomplishment and I would table
the project for later. Over time, there were so many projects like this that it
became a personal mission to finish as many projects as possible. I went back
and finished several in-progress projects and went on to start and then finish
many more. I became hungry for "checkboxes" as I used to think of them. As the
years went by I noticed that very few of my finished projects were games. After
all the time I spent learning about games and game technology, this did not feel
great. I felt I needed to have something to show for the knowledge I accumulated
about games in the 11 years I've been programming.

I was ready for a change and decided that this would be my last "from-scratch"
(as in, without a game engine) game I would do by myself. I set out to make a
multiplayer experience with simple cuboid walls and billboard sprites.

## The Design of Boxels
- Defining Boxels: Pixels, Voxels, Bloxels, and Boxels
- High-Level Game Design

Boxels refer to a nomenclature I have developed over the years:

* Pixels: containers for a specific color in a 2D image
* Voxels: volumetric pixels
* Bloxels: isometric 2.5D voxel sprites
* Boxels: textured cubes large enough for one game entity to stand in

The design of the game involved a client that handles player input, sound,
resource loading, and graphics, and a server that would handle the gameworld
simulation with physics, player -> entity tracking, and map generation.

## Development Timeline

I created boxels in 15 day's time working in the evenings and weekends for a
total of approximately 30 hours of work on 12 separate days.

<pre>
    <div class="mermaid">
        %%{
            init: {
                'logLevel': 'debug',
                'theme': 'default',
                'themeVariables': {
                    'cScale0': '#A0522D',
                    'cScale1': '#8A3324',
                    'cScale2': '#6B8E23',
                    'cScale3': '#8A9A5B',
                    'cScale4': '#9EA587',
                    'cScale5': '#E97451'
                }
            }
        }%%
        timeline
            title Timeline of Project Boxels: Week 1
            Day 1 [7/3/23]: Raylib hello world example up and running
            Day 2 [7/4/23]: Textured boxel model
                : Perspective camera
                : Boxel <-> Entity collisions
                : Walking around in world
            Day 3 [7/5/23]: Billboard sprites
                : Entity <-> Entity collisions
            Day 4 [7/6/23]: Attempted Rendezvous Server for NAT punchthrough
            Day 5 [7/7/23]: Attempted using TCP & UDP together
                : Adopted TCP event transport
                : Added message protocol
                : Multiple players connected
            Day 6 [7/8/23]: Created game object model
                : Moving entities over network
    </div>
</pre>

<pre>
    <div class="mermaid">
        %%{
            init: {
                'logLevel': 'debug',
                'theme': 'default',
                'themeVariables': {
                    'cScale0': '#A0522D',
                    'cScale1': '#8A3324',
                    'cScale2': '#6B8E23',
                    'cScale3': '#8A9A5B',
                    'cScale4': '#9EA587',
                    'cScale5': '#E97451'
                }
            }
        }%%
        timeline
            title Timeline of Project Boxels: Week 2
            Day 7 [7/9/23]: Players see each other
            Day 8 [7/11/23]: Created stoppable asynchronous Task system
            Day 9 [7/12/23]: 3D audio concept
                : Gamepad input
                : Rewrote networking to use task system
            Day 10 [7/13/23]: Player name labels
                : Clients receive map with 6-sided boxels
                : 3D audio complete
            Day 11 [7/14/23]: Networked physics with FCL
            Day 12 [7/15/23]: Non-player entities
                : Created test map with AI generated textures
                : Generated final build using Nuitka
    </div>
</pre>

3D audio took me almost an entire day.
Physics took me an entire day.
Networking took me 3 days and I rewrote it 3 times.
I tried 2 different networking techniques to no avail: a
public rendezvous server for NAT Punchthrough and using TCP and UDP together.

Wire protocol vs message protocol.

I rapid prototyped the project using [Kenny's](https://kenney.nl/) free assets.
This helped make the beginning of the project more enjoyable as there was
something to render on screen from day one.

## Technical Components
- Tools and Libraries Used
- Python, Raylib, and more
- From-scratch TCP socket networking
- By-hand 3D audio
- Use of ChatGPT as a coding assistant

- The entire game is **1578** lines of Python code (2158 if you include comments
    and whitespace). This is an astonishing number because this is a 3D
    multiplayer experience, not a command line application. People really seem
    to underestimate Python. Sometimes for good reason, other times it just
    baffles me how hard some tasks are in other languages when I've seen good
    designs that have existed in Python for years before being adopted
    elsewhere.

## Challenges Encountered
- Python's dynamic typing challenge
- Cross-platform limitations

- There is no cross-platform way to get the MTU in any language!
- NAT Punchthrough is not 100% reliable, especially not with VPNs in between.
- Multiplayer networking is an entirely separate project at least the size of
    the game client.
- Wire protocol is different than message protocol
- Python's dynamic typing was really difficult when the project got larger. I
    couldn't believe the sensation. It was as if as soon as the project got to
    be slightly larger than I could hold in my brain, I literally felt something
    fall out of my working memory and I had to go and find what it was and get
    it back in there.
- ChatGPT as a coding assitant (both more and less useful than people think)
    Took me all of my 11 years of practice and an AI assistant to do this in 13
    days. People think that the usage of AI makes things effortless but in
    reality it took many prompts and 11 years of coding experience to make this
    project.
- Dynamic typing combined with metaprogramming made for a powerful design for
    the event system. However, it was also challenging to debug the project as
    it grew.

## Networking
- Network Design: Messaging Model
- Networking Techniques: TCP and UDP, NAT Punchthrough
- Wire Protocol vs Message Protocol

On the server, connections were tracked by address and handled in their own
task.

## Game Building Blocks
- Entity System and Future Extensions
- Project Prototyping with Free Assets

## Asynchronous Programming
- Creation and Utility of Stoppable Task System
- Python Threading

Asynchrony was harnessed through the creation of a stoppable task type that took
advantage of Python generators to yield at key stopping points in the thread
handler function. Cleanup code could then examine which checkpoint was last
yielded to see what resources needed to be freed. The server transport, client
handler, and client transport all used the task type in order to run code in a
separate thread. All the usual Python threading caveats apply, although a useful
feature of the task class was a built in way to send and receive messages from
outside and inside the task. This provided a very flexible base upon which to
build complex raw socket handling code while utilizing Python's ability to get
parallelism with IO tasks.

TODO(pbz): Create mermaid diagrams for this stuff.

## Client-Server Model
- Client Responsibilities
- Server Responsibilities

## Event/Messaging System
- Use of Pydantic and MessagePack
- Quick Update Type and Deduplication

TODO(pbz): Create mermaid diagrams for this stuff.

Both the client and the server made use of a custom networking facility that
used raw TCP sockets. To send structured data back and forth, an event/messaging
model was created by using Pydantic models serialized to JSON and encoded with
MessagePack which greatly reduced their size. Events were effectively type
checked as constructing one with incorrect data types was impossible using
Pydantic.

TODO(pbz): Create mermaid diagrams for this stuff.

Events also took advantage of the mixin class design pattern by inheriting from
a quick update type that would demarcate that event as eligible for
deduplication in situations where the network was unable to keep up with the
amount of those events being sent. This worked extremely well and made it so
that only one player input or entity update event was ever sent over the wire.
Since the events already used Pydantic, adding a new event type was as simple
as inheriting one or two classes and adding annotated fields.

## GameObject Model
- Server and Client Game Object Model
- Object Model Modification and Event Communication

The game object model was maintained by the server and mirrored on the client.
Modifications to the model during runtime were communicated via one-shot or
frame-by-frame events. The map was only update upon modification and the current
position of entities and connected players was sent every frame. The object
model was simple in that there were only ever 3 types, one for the player,
entities, and boxels. More types would have eventually been needed to structure
and store more data, however, as dictionaries formed the backbone of the client
and server's game object storage.

## Graphics and Input
- Rendering with Raylib
- Gamepad Input Management

Input was gathered using Raylib. Gamepad input was extremely easy to obtain and
manage. Graphics were rendered using Raylib.

## 3D Boxel Design
- Designing 3D Boxels with Blender
- Texture Management and Caching

Boxels are designed to support a different texture on each of the 6 sides and be
about the size of one entity in the game. This makes it so that levels can be
created quickly while still feeling big enough. I found that with voxels, each
"volumetric pixel" is too granular and basically requires outdoor areas to make
use of procedural generation.

The 3D boxels themselves were loaded from a mesh created in Blender containing
6 quads made of 2 coplanar triangles, each with UV coordinates mapped to a
spritesheet laid out with room for 6 textures along the X axis. The boxel model
was loaded once but then each unique combination of boxel side textures was
drawn to an image and uploaded to the GPU for use during rendering. In this way,
boxels using the same texture could be batched by Raylib and there was ever only
1 mesh in play aside from the quads submitted by Raylib for billboard sprites,
fonts, and debug geometry. When drawn to an image during runtime, they would
look like this:

![Boxel Texture](../static/img/boxel-texture.png)

![Boxel Texture Annotated](../static/img/boxel-texture-annotated.png)

Specifying side textures to cache used these combinations:

* All sides
* Top, rest of sides
* Top, bottom, rest of sides
* Top, bottom, left, right, front, back


## Conclusion
- Personal Reflections
- Future Plans for Boxels

> **Key Takeaways**
> * One
> * Two

## Appendix
- Libraries Used
- Project Images and Diagrams

**Libraries Used:**

* Raylib (windowing, rendering, input, audio, timing)
* Flexible Collision Library (collision detection & response)
* Pydantic (marshalling events back and forth)
* MessagePack (compressing events back and forth)
* MeowHash Python (bindings to MeowHash written by me)
* Nuitka (compiling the game to an executable)


---

<abbr title="Transmission Control Protocol">TCP</abbr>

---

![Boxel Screenshot](../static/img/boxels-screenshot-2.png)

![Boxel Screenshot](../static/img/boxels-screenshot-1.png)
