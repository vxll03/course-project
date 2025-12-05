const isSecured = false
const protocol = isSecured ? 'https://' : 'http://'
const ip = 'localhost'

const bookBase = `${protocol}${ip}:8002/bookshop`;
const chatBase = `${protocol}${ip}:8001/chat`;
const authBase = `${protocol}${ip}:8000/auth`;

export { bookBase, chatBase, authBase };