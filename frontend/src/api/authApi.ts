import { api } from "./base/axiosinstance";
import { authBase } from "./base/paths";

export const register = async (
  username: string,
  password: string,
  passwordRepeat: string
) =>
  await api.post(
    `${authBase}/register/`,
    {
      username: username,
      password: password,
      password_repeat: passwordRepeat,
    },
    { withCredentials: true }
  );

export const login = async (username: string, password: string) =>
  await api.post(
    `${authBase}/token/create/`,
    {
      username: username,
      password: password,
    },
    { withCredentials: true }
  );

export const logout = async () => await api.post(`${authBase}/token/delete/`);

export const check = async () => await api.get(`${authBase}/health_check/`);

export const getUserById = async (id: number) =>
  await api.get(`${authBase}/users/${id}`);

export const getCurrentUser = async () =>
  await api.get(`${authBase}/users/me/`, { withCredentials: true });
