import fs from 'fs';

import sheet from './sheet';

type ISection = {
  topic: string;
  topicTitle: string;
  title: string;
  sectionId: string;
};

interface ITechnologyJSON {
  languages: ISection;
  frameworks: ISection;
  tools: ISection;
  databases: ISection;
  platforms: ISection;
}

(async () => {
  const technologies: ITechnologyJSON = JSON.parse(
    fs.readFileSync('./spider/technologies.json', 'utf-8'),
  );

  const [languages, frameworks, tools, databases, platforms] = Object.values(
    technologies,
  ).map(technology => technology.map((section: ISection) => section));

  await sheet({
    cells: [...languages, ...frameworks, ...tools, ...databases, ...platforms],
  });
})();
