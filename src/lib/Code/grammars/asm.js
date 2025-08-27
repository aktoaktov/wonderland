const opcodes = new RegExp("\\b(?:" + [
  /* Данные */ "mov",
  /* Управление */ "jmp", "ret",
  /* Сложение */ "add", "sub", "inc", "dec",
  /* Умножение */ "mul", "imul",
].join('|') + ")\\b")

let asm = {
  'comment': /;.*/,
  'directive': {
    pattern: /\.\w+(?= )/,
    alias: 'property',
  },
  'string': /(["'`])(?:\\.|(?!\1)[^\\\r\n])*\1/,
  'op-code': {
    pattern: opcodes,
    alias: 'keyword',
  },
  'hex-number': {
    pattern: /#?\$[\da-f]{1,4}\b/i,
    alias: 'number',
  },
  'binary-number': {
    pattern: /#?%[01]+\b/,
    alias: 'number',
  },
  'decimal-number': {
    pattern: /#?\b\d+\b/,
    alias: 'number',
  },
  'register': {
    pattern: /\b[re]?[abcd][xhl]\b/,
    alias: 'variable',
  },
  'punctuation': /[(),:]/,
}

export default asm