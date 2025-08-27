<script>
    import {randRange, randChoice, Vector, _range} from "../utilities.js"
    import {onMount} from "svelte"
    import Button from "$lib/Elements/Button.svelte"

    let canvas
    let context

    const WIDTH = 800
    const HEIGHT = 600

    const PARTICLE_SIZE = 10
    const PARTICLE_COUNT = 1000


    let particles = []
    let goal = new Vector(WIDTH - 30, HEIGHT - 30)

    onMount(() => {
        canvas.width = WIDTH
        canvas.height = HEIGHT

        const offscreen = canvas.transferControlToOffscreen()
        context = offscreen.getContext("2d")
    })

    class Particle {
        constructor(x, y, vX = 0, vY = 0) {
            this.position = new Vector(x, y)
            this.velocity = new Vector(vX, vY)
            this.pBest = new Vector(x, y)
        }

        reset(outwards) {
            this.velocity = new Vector(outwards * (-1 + (2 * Math.random())), outwards * (-1 + (2 * Math.random())))
            this.pBest = new Vector(this.position.x, this.position.y)
            this.update()
        }

        update() {
            let error = f(this.position)

            if (error < f(this.pBest)) {
                this.pBest = this.position
            }

            if (error < f(gBest)) {
                gBest = this.position
            }

            this.position.x = this.position.x + this.velocity.x
            this.position.y = this.position.y + this.velocity.y

            let r1 = Math.random()
            let r2 = Math.random()
            this.velocity.x = w * this.velocity.x + c1 * r1 * (this.pBest.x - this.position.x) + c2 * r2 * ((gBest.x || this.position.x) - this.position.x)
            this.velocity.y = w * this.velocity.y + c1 * r1 * (this.pBest.x - this.position.y) + c2 * r2 * ((gBest.y || this.position.x) - this.position.y)

            if (this.position.x >= WIDTH - 1) {
                this.position.x = WIDTH - 1
                this.velocity.x *= -1
            }
            if (this.position.y >= HEIGHT - 1) {
                this.position.y = HEIGHT - 1
                this.velocity.y *= -1
            }
            if (this.position.x <= 0) {
                this.position.x = 0
                this.velocity.x *= -1
            }
            if (this.position.y <= 0) {
                this.position.y = 0
                this.velocity.y *= -1
            }
        }

        draw() {
            context.beginPath()
            context.fillStyle = `black`
            context.arc(this.position.x, this.position.y, 1, 0, Math.PI * 2)
            context.fill()
            context.closePath()
        }
    }

    function f(x, y) {
        return Math.sqrt(Math.pow(target.x - x, 2) + Math.pow(target.y - y, 2))
    }

    let target = $state(new Vector(WIDTH / 2, HEIGHT / 2))

    let gBest = $state(new Vector(0, 0))


    let w = 0.9
    let c1 = 0.1
    let c2 = 0.1
    let splat = 0.1

    let m = false

    function distance(x1, y1, x2, y2) {
        return Math.sqrt(Math.pow(x1 - x2, 2) + Math.pow(y1 - y2, 2))
    }


    let lastTargetX
    let lastTargetY


    const onmousedown = (event) => {
        const rect = canvas.getBoundingClientRect()
        const x = event.clientX - rect.left
        const y = event.clientY - rect.top

        if (x >= 0 && x <= WIDTH && y >= 0 && y <= HEIGHT) {
            lastTargetX = target.x
            lastTargetY = target.y
            target.x = x
            target.y = y

            gBest.x = 0
            gBest.y = 0

            particles.forEach(element => {
                element.reset(splat * distance(target.x, target.y, lastTargetX, lastTargetY))
            })
        }
    }


    const start = () => {
        target.x = WIDTH / 2
        target.y = HEIGHT / 2
        lastTargetX = WIDTH / 2
        lastTargetY = HEIGHT / 2

        for (let i = 0; i < PARTICLE_COUNT; i++) {
            particles.push(new Particle(parseInt(WIDTH * (-1 + (2 * Math.random()))), parseInt(HEIGHT * (-1 + (2 * Math.random()))), 5 * (-1 + (2 * Math.random())), 5 * (-1 + (2 * Math.random()))))
        }

        function animate() {
            requestAnimationFrame(animate)
            context.clearRect(0, 0, canvas.width, canvas.height)

            for (let particle of particles) {
                particle.draw()
                particle.update()
            }
        }

        animate()
    }
</script>


<Button onclick={start}>Старт</Button>

<!--<input type="range" bind:value={}/>-->
<br/>

<canvas bind:this={canvas}></canvas>