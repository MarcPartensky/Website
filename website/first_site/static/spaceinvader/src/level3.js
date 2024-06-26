class Level3 extends Level {
    constructor() {
        super()
        this.over = false
        this.group = new Group([
            [
                'playerMissileGroup',
                new MissileGroup()
            ],
            [
                'enemyMissileGroup',
                new MissileGroup()
            ],
            [
                'player',
                new Player(
                    new Square(0, 0, 0.05, 'blue', 0.01, true),
                    new Body(new Motion(new Vector(0.5, 0.9), new Vector(0, 0)))
                )
            ],
            [
                'enemyGroup',
                new EnemyGroup([
                    [
                        'enemy1',
                        new Enemy(
                            new Circle(new Vector(0, 0), 0.02, 0.01, 'red'),
                            new Body(new Motion(new Vector(1/8, 0.1), new Vector(0.2, 0)))
                        )
                    ],
                    [
                        'enemy2',
                        new Enemy(
                            new Circle(new Vector(0, 0), 0.02, 0.01, 'red'),
                            new Body(new Motion(new Vector(2/8, 0.1), new Vector(0.2, 0)))
                        ),
                    ],
                    [
                        'enemy3',
                        new Enemy(
                            new Circle(new Vector(0, 0), 0.02, 0.01, 'red'),
                            new Body(new Motion(new Vector(3/8, 0.1), new Vector(0.2, 0)))
                        )
                    ],
                    [
                        'enemy4',
                        new Enemy(
                            new Circle(new Vector(0, 0), 0.02, 0.01, 'red'),
                            new Body(new Motion(new Vector(4/8, 0.1), new Vector(0.2, 0)))
                        ),
                    ],
                    [
                        'enemy5',
                        new Enemy(
                            new Circle(new Vector(0, 0), 0.02, 0.01, 'red'),
                            new Body(new Motion(new Vector(5/8, 0.1), new Vector(0.2, 0)))
                        ),
                    ],
                    [
                        'enemy6',
                        new Enemy(
                            new Circle(new Vector(0, 0), 0.02, 0.01, 'red'),
                            new Body(new Motion(new Vector(6/8, 0.1), new Vector(0.2, 0)))
                        ),
                    ],
                    [
                        'enemy7',
                        new Enemy(
                            new Circle(new Vector(0, 0), 0.02, 0.01, 'red'),
                            new Body(new Motion(new Vector(7/8, 0.1), new Vector(0.2, 0)))
                        ),
                    ]
                ])
            ]
        ])
        this.border = new Square(0, 0, 1, 'grey', 0.01, false)
        this.line = new Segment(new Point(0, 0.7), new Point(1, 0.7), 1, 'darkgrey')
    }
    isWon() {
        return this.group.get('enemyGroup').size == 0
    }
}
