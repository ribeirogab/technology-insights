import request from 'request-promise';
import cheerio from 'cheerio';

interface ISpiderProps {
  sectionId: string;
}

interface ITechnology {
  name: string;
  percentage: number;
}

export default async ({ sectionId }: ISpiderProps): Promise<ITechnology[]> => {
  const technologies: ITechnology[] = [];

  await request(
    'https://insights.stackoverflow.com/survey/2020',
    (err, res, body) => {
      if (err) console.log(`Error: ${err}`);

      const $ = cheerio.load(body);

      $(`#${sectionId} tbody tr`).each((index, element) => {
        const name = $(element).find('.label').text().replace(/\s\s+/g, '');
        const percentage = Number(
          $(element)
            .find('.bar span')
            .text()
            .replace(/\s/g, '')
            .replace('%', ''),
        );

        technologies.push({ name, percentage });
      });
    },
  );

  return technologies;
};
