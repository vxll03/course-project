interface IAuthor {
  name: string
  text?: string
  bookCount: number
}

interface IBook {
  id: number
  title: string
  text: string
  price: number
  img?: string
}

interface CurrentBook {
  id: number
  title: string
  description: string
  price: number
  img?: string
  author: string
}

interface Message{
  id: number
  text: string
  timestamp: string
  author: number
  type: string
}

interface ChatHistory {
  id: number
  name: string
  messages: Array<Message | null> 
}

export type { IAuthor, IBook, CurrentBook, Message, ChatHistory }