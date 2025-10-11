import { api } from "./base/axiosinstance";
import { bookBase } from "./base/paths";

export const getAuthors = async () =>
  await api.get(`${bookBase}/authors/`);

export const getAuthorById = async (id: number) =>
  await api.get(`${bookBase}/authors/${id}`);