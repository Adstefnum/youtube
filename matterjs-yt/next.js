// module aliases
var Engine = Matter.Engine,
    Render = Matter.Render,
    Runner = Matter.Runner,
    Bodies = Matter.Bodies,
    Composite = Matter.Composite,
    Mouse = Matter.Mouse,
    MouseConstraint = Matter.MouseConstraint;

// create an engine
var engine = Engine.create();

// create a renderer
var render = Render.create({
    element: document.body,
    engine: engine
});

// create two boxes and a ground
var ground = Bodies.rectangle(400, 610, 810, 60, { isStatic: true });
var leftWall = Bodies.rectangle(0, 305, 10, 610, { isStatic: true });
var rightWall = Bodies.rectangle(800, 305, 10, 610, { isStatic: true });

// add all of the bodies to the world
Composite.add(engine.world, [ground, leftWall, rightWall]);

// add mouse control
var mouse = Mouse.create(render.canvas),
    mouseConstraint = MouseConstraint.create(engine, {
        mouse: mouse,
        constraint: {
            stiffness: 0.2,
            render: {
                visible: false
            }
        }
    });

Composite.add(engine.world, mouseConstraint);



// add new bodies with mouse click
document.addEventListener('mousedown', function(event) {
    var position = {
        x: event.clientX,
        y: event.clientY
    };

    if (!event.ctrlKey && event.button === 2) {
        var box = Bodies.rectangle(position.x, position.y, 80, 80);
        Composite.add(engine.world, box);
    }

    else if (event.ctrlKey && event.button === 2) {
        var ball = Bodies.circle(position.x, position.y, 40);
        Composite.add(engine.world, ball);
    }
});
// create runner
var runner = Runner.create();

// run the engine
Runner.run(runner, engine);
// run the renderer
Render.run(render);
