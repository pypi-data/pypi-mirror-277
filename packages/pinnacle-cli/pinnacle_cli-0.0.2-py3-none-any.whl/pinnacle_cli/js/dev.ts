import express from "express";
import fs from "fs";
import path from "path";
import cors from "cors";
import constants from "./constants";

const app = express();
app.use(cors());
app.use(express.json());

const cwd = process.argv[2];
const pinnacleDirectory = `${cwd}/${constants.DIRECTORY}`;

var files;
try {
  files = fs.readdirSync(pinnacleDirectory);
} catch (error) {
  console.error(`Error reading directory: ${error}`);
  process.exit(1);
}

const endpoints_data = {};

files.forEach((file: string) => {
  const ext = path.extname(file);
  if (ext === ".js" || ext === ".ts") {
    var functionModule;
    try {
      functionModule = require(path.join(pinnacleDirectory, file));
    } catch (error) {
      console.error(`Error requiring file: ${file}, ${error}`);
      return;
    }
    const functions = Object.getOwnPropertyNames(functionModule).filter(
      (prop) => typeof functionModule[prop] === "function"
    );

    functions.forEach((func) => {
      const callableFunction = functionModule[func];
      endpoints_data[func] = "";
      app.post(`/${func}`, (req: express.Request, res: express.Response) => {
        const result = callableFunction(...Object.entries(req.body));
        res.send({ data: result });
      });
    });
  }
});

const file_path = `${pinnacleDirectory}/.metadata/js_endpoints.json`;
fs.writeFileSync(file_path, JSON.stringify(endpoints_data));

app.listen(constants.JAVASCRIPT_PORT);
