const accent: string = "#07a9de";
const greenAccent: string = "#42b883";
const white: string = "#FFFFFF";
const gray: string = "#F0F0F0";
const black: string = "#000000";

export interface ColorSet {
  background: string;
  foreground: string;
  border: string;
  unpack(): Object;
}

function unpack(this: ColorSet) {
  return {
    "--back": this.background,
    "--border": this.border,
    "--fore": this.border,
  };
}

const mainColor: ColorSet = {
  border: accent,
  foreground: accent,
  background: white,
  unpack,
};
const greenColor: ColorSet = {
  border: greenAccent,
  foreground: greenAccent,
  background: white,
  unpack,
};
const grayColor: ColorSet = {
  border: gray,
  foreground: black,
  background: gray,
  unpack,
};

export { mainColor, greenColor, grayColor };
