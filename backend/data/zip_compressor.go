package main

import (
	"archive/zip"
	"io"
	"os"
)

func main() {
	inputFile := "cybersecurity_data.json"
	outputZip := "cybersecurity_data.zip"

	zipFile, err := os.Create(outputZip)
	if err != nil {
		panic(err)
	}
	defer zipFile.Close()

	archive := zip.NewWriter(zipFile)
	defer archive.Close()

	fileToZip, err := os.Open(inputFile)
	if err != nil {
		panic(err)
	}
	defer fileToZip.Close()

	info, err := fileToZip.Stat()
	if err != nil {
		panic(err)
	}

	header, err := zip.FileInfoHeader(info)
	if err != nil {
		panic(err)
	}

	header.Name = inputFile
	header.Method = zip.Deflate

	writer, err := archive.CreateHeader(header)
	if err != nil {
		panic(err)
	}

	_, err = io.Copy(writer, fileToZip)
	if err != nil {
		panic(err)
	}
}
