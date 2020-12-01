import excel from 'excel4node';
import cliProgress from 'cli-progress';
import colors from 'colors';

import spider from './spider';

export type ISection = {
  topic: string;
  topicTitle: string;
  title: string;
  sectionId: string;
};

export interface ISheetProps {
  cells: ISection[];
}

export default async ({ cells }: ISheetProps): Promise<void> => {
  const workbook = new excel.Workbook();

  const progressBar = new cliProgress.SingleBar({
    format: `Cells Progress |${colors.green(
      '{bar}',
    )}| {percentage}% || {value}/{total} Cells`,
    barCompleteChar: '\u2588',
    barIncompleteChar: '\u2591',
    hideCursor: true,
  });

  progressBar.start(cells.length, 0);

  for (let i = 0; i < cells.length - 1; i++) {
    progressBar.update(i + 1);

    const worksheet = workbook.addWorksheet(cells[i].title);
    const rows = await spider({ sectionId: cells[i].sectionId });

    worksheet.cell(1, 1).string('tech');
    worksheet.cell(1, 2).string('percentage');

    rows.forEach((row, index) => {
      worksheet.cell(index + 2, 1).string(row.name);
      worksheet.cell(index + 2, 2).number(row.percentage);
    });
  }

  progressBar.update(20);
  progressBar.stop();
  workbook.write(`./data/data.xlsx`);
};
