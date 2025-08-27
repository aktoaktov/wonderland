<script>
    import {randRange, randChoice, Vector, _range} from "../utilities.js"
    import {onMount} from "svelte"
    import Button from "$lib/Elements/Button.svelte"

    let canvas
    let context

    let BROADCAST_DISTANCE = $state(50)
    let TARGET_SPEED = $state(0.5)

    let FINITE_RESOURCES = $state(false)

    const WIDTH = 800
    const HEIGHT = 600


    const CELL_COUNT = 1000
    const CELL_SIZE = 1

    const MIN_CELL_SPEED = 1
    const MAX_CELL_SPEED = 2

    const TARGET_SIZE = 20

    let beings = []
    let targets = []

    onMount(() => {
        canvas.width = WIDTH
        canvas.height = HEIGHT

        const offscreen = canvas.transferControlToOffscreen()
        context = offscreen.getContext("2d")
    })

    class Target {
        constructor(color) {
            this.position = new Vector(Math.random() * WIDTH, Math.random() * HEIGHT)
            this.direction = Vector.fromRandom()
            this.velocity = TARGET_SPEED
            this.size = TARGET_SIZE
            this.color = color
        }

        draw() {
            context.beginPath()
            context.fillStyle = `hsl(${this.color}, 100%, 25%)`
            context.arc(this.position.x, this.position.y, this.size, 0, Math.PI * 2)
            context.fill()
            context.closePath()
        }

        animate() {
            this.draw()

            this.position.x += this.direction.x * this.velocity
            this.position.y += this.direction.y * this.velocity

            if (this.position.x <= 0 || this.position.x >= canvas.width) {
                this.direction.x *= -1
            }

            if (this.position.y <= 0 || this.position.y >= canvas.height) {
                this.direction.y *= -1
            }
        }
    }

    class Being {
        constructor(x, y, size) {
            this.position = new Vector(x, y)
            this.size = size
            this.velocity = randRange(MIN_CELL_SPEED, MAX_CELL_SPEED)
            this.direction = new Vector(randRange(-1, 1), randRange(-1, 1)).getNormalized()
            this.id = Math.random()
            this.broadcastHighlight = false

            this.objectiveDest = Math.floor(randRange(0, targets.length))
            this.color = targets[this.objectiveDest].color

            this.distanceFromDest = []
            this.broadcast = []

            targets.forEach((_, index) => {
                this.distanceFromDest[index] = 1_000
                this.broadcast[index] = 1_000
            })

        }


        draw() {
            context.beginPath()
            context.fillStyle = `hsl(${this.color}, 100%, 25%)`
            context.arc(this.position.x, this.position.y, this.size, 0, 2 * Math.PI)
            context.fill()
            context.closePath()
        }


        isCollidingWith(being) {
            return this.position.distanceTo(being.position) <= this.size + being.size
        }


        drawConnection(being, targetIndex) {
            context.beginPath()
            context.strokeStyle = `hsl(${targets[targetIndex].color}, 100%, 25%, 0.4)`
            context.lineWidth = 1.0
            context.moveTo(being.position.x, being.position.y)
            context.lineTo(this.position.x, this.position.y)
            context.stroke()
            context.closePath()
        }


        animate() {
            this.draw()

            let broadcastDist = BROADCAST_DISTANCE
            this.direction.x += randRange(-0.05, 0.05)
            this.direction.y += randRange(-0.05, 0.05)

            for (let i = 0; i < targets.length; i++) {
                this.distanceFromDest[i]++
            }

            for (let i = 0; i < targets.length; i++) {
                if (this.isCollidingWith(targets[i])) {
                    this.distanceFromDest[i] = 0

                    if (this.objectiveDest === i) {

                        if (FINITE_RESOURCES) {
                            if (i === 0 || i === 1) {
                                // targets[i].size += 0.01
                            } else {
                                if (targets[i].size > 0.1) {
                                    targets[i].size -= 0.05
                                } else {
                                    targets[i] = new Target(Math.floor(randRange(180, 360)))
                                }
                            }

                        }

                        this.color = targets[this.objectiveDest].color

                        this.direction = this.direction.mul(-1)

                        let closestQueen = this.position.distanceTo(targets[0].position) < this.position.distanceTo(targets[1].position) ? 0 : 1
                        this.objectiveDest = i === 0 ? randChoice(_range(2, targets.length)) : i === 1 ? randChoice(_range(2, targets.length)) : closestQueen
                    }
                }
            }

            this.broadcast = []
            targets.forEach((item, index) => this.broadcast.push(this.distanceFromDest[index] + broadcastDist))

            let being

            for (being of beings) {
                if (this.position.distanceTo(being.position) <= broadcastDist) {
                    for (let i = 0; i < targets.length; i++) {
                        if (being.broadcast[i] < this.distanceFromDest[i]) {
                            this.distanceFromDest[i] = being.broadcast[i]

                            if (this.broadcastHighlight === true) {
                                this.drawConnection(being, i)
                            }

                            if (this.objectiveDest === i) {
                                let n = this.position.directionTo(being.position)
                                if (n.x) {
                                    this.direction = this.position.directionTo(being.position)
                                }
                            }
                        }
                    }
                }
            }

            this.position.x += this.direction.x * this.velocity
            this.position.y += this.direction.y * this.velocity


            if (this.position.x <= 0 || this.position.x >= canvas.width) {
                this.direction.x *= -1
            }

            if (this.position.y <= 0 || this.position.y >= canvas.height) {
                this.direction.y *= -1
            }
        }
    }

    const start = () => {
        targets.splice(0)
        beings.splice(0)

        targets.push(new Target(60))
        targets.push(new Target(50))
        targets.push(new Target(240))
        targets.push(new Target(180))

        for (let i = 0; i < CELL_COUNT; i++) {
            let being = new Being(Math.random() * canvas.width, Math.random() * canvas.height, CELL_SIZE)
            beings.push(being)
        }

        // function enableBroadcastHighlight() {
        beings.forEach((being) => being.broadcastHighlight = true)

        // }


        function disableBroadcastHighlight() {
            beings.forEach((being) => being.broadcastHighlight = false)
        }


        function animate() {
            requestAnimationFrame(animate)
            context.clearRect(0, 0, canvas.width, canvas.height)

            for (let target of targets) {
                target.animate()
            }

            for (let being of beings) {
                being.animate()
            }
        }

        animate()

    }

</script>


<Button onclick={start}>Старт</Button>

<input type="range" bind:value={BROADCAST_DISTANCE}/>
<!--<input bind:value={TARGET_SPEED} />-->
<!--<Checkbox/>-->
<input type="checkbox" bind:checked={FINITE_RESOURCES}/>

<canvas bind:this={canvas}></canvas>