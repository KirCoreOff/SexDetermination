import os

import numpy
import openpyxl
import xlsxwriter
import face_recognition
import numpy as np


def recognition(training): #ф=ия для создания тестового множества
    images = os.listdir("img")
    for i in range(0, 128): #заполняется эксель
        training.write(0, i, f"X{i+1}")
    training.write(0, 128, "D1")

    row = 1
    for image in images:    #на всех фотографиях в папке
        face = face_recognition.load_image_file(f"img/{image}") #ищется лицо
        code = face_recognition.face_encodings(face)[0] #кодируется лицо
        for i in range(0, len(code)):   #и записывается в ексель файл
            training.write(row, i, code[i])
        training.write(row, 128, image[0])  #первым символом в имени фотографии является фактический пол человека, расположенного на фотографии (задаеися при добавлении фотографии в папку)
        row += 1
        print(f"[INFO] {row-1}/{len(os.listdir('img'))}")

    print("[INFO] TRAINING DATA CREATED SUCCESSFULLY!\n")


def test_data(test):    #все то же самое, что и в предыдущий функции, только для создания проверочного множетсва
    for i in range(0, 128):
        test.write(0, i, f"X{i}")
    test.write(0, 128, "D1")
    row = 1
    images = os.listdir("test")
    for image in images:
        face = face_recognition.load_image_file(f"test/{image}")
        code = face_recognition.face_encodings(face)[0]
        for i in range(0, len(code)):
            test.write(row, i, code[i])
        test.write(row, 128, image[0])
        # test.write(row, 0, image[1:-4])
        row += 1
        print(f"[INFO] {row-1}/{len(os.listdir('test'))}")
        print(image[1:-4])
        print()
    print("[INFO] TEST DATA CREATED SUCCESSFULLY!")


def main():
    book = xlsxwriter.Workbook("dataset.xlsx") #создание эксель файла
    training = book.add_worksheet("training") #создание странички эксель с тестовым множеством
    test = book.add_worksheet("test")   #создание странички ексель с проверочным множеством
    recognition(training)
    test_data(test)
    book.close()


if __name__ == '__main__':
    main()


