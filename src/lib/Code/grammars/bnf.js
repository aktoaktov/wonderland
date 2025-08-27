let bnf = {
    'string': {
        pattern: /"[^\r\n"]*"|'[^\r\n']*'/,
    },
    'definition': {
        pattern: /<[^<>\r\n\t]+>(?=\s*::=)/,
        alias: ['keyword', 'syntaxes'],
        inside: {
            'punctuation': /^<|>$/,
        },
    },
    'syntaxes': {
        pattern: /<[^<>\r\n\t]+>/,
        inside: {
            'punctuation': /^<|>$/,
        },
    },
    'operator': /::=|[|()[\]{}*+?]|\.{3}/,
}

export default bnf
