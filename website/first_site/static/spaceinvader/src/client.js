const ticks = 10
const canvas = document.getElementById('canvas')
const levels = [Level1, Level2, Level3]
const game = new Game(ticks, canvas, levels)
game.context.plane.units.position = new Vector(700, 700)
game.context.plane.location.position = new Vector(0.5, 0.5)
game.main()
