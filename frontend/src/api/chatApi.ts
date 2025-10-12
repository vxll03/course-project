import { api } from "./base/axiosinstance";
import { chatBase } from "./base/paths";

export const getChatHistory = async (chatName: string) =>
  await api.get(`${chatBase}/history/${chatName}/`);

export const getGeneralChat = async () =>
  await api.get(`${chatBase}/history/general/`)