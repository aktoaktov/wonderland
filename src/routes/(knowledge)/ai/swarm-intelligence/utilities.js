export function randRange(min, max) {
    return Math.random() * (max - min) + min
}


export function randChoice(arr) {
    return arr[Math.floor(Math.random() * arr.length)];
}


export function range(n) {
    let arr = []

    for (let i = n; i > 0; i--) {
        arr.push(0)
    }

    return arr
}


export function _range(min, max) {
    return [...Array(max - min).keys()].map((n) => n + min)
}


export class Vector {
    constructor(x, y) {
        this.x = x;
        this.y = y;
    }

    static fromOne(n) {
        return new Vector(n, n)
    }

    static fromMagnitude(magnitude, direction) {
        direction = direction.getNormalized();
        return direction.mul(magnitude);
    }

    static fromRandom() {
        return new Vector(Math.random(), Math.random()).getNormalized();
    }

    add(vec) {
        return new Vector(this.x + vec.x, this.y + vec.y);
    }

    sub(vec) {
        return new Vector(this.x - vec.x, this.y - vec.y);
    }

    mul(n) {
        return new Vector(this.x * n, this.y * n);
    }

    div(n) {
        return new Vector(this.x / n, this.y / n);
    }

    distanceTo(vec) {
        let xd = Math.abs(this.x - vec.x)
        let yd = Math.abs(this.y - vec.y)

        return Math.sqrt(Math.pow(xd, 2) + Math.pow(yd, 2))
    }

    directionTo(vec) {
        return vec.sub(this).getNormalized()
    }

    magnitude() {
        return Math.sqrt(Math.pow(this.x, 2) + Math.pow(this.y, 2));
    }

    getNormalized() {
        return new Vector(this.x / this.magnitude(), this.y / this.magnitude());
    }

    isSameAs(vec) {
        return this.x === vec.x && this.y === vec.y;
    }
}

