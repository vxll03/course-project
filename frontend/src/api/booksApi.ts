import { api } from "./base/axiosinstance";
import { bookBase } from "./base/paths";

export const getBooks = async () =>
  await api.get(`${bookBase}/books/`);

export const getBookById = async (id: number) =>
  await api.get(`${bookBase}/books/${id}`);