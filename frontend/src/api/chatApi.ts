import { api } from "./base/axiosinstance";
import { chatBase } from "./base/paths";

export const getBooks = async () =>
  await api.get(`${chatBase}//`);