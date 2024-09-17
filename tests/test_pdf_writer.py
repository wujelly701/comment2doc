# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@ File       : test_pdf_writer.py
@ Time       ：2024/9/12 1:59
@ Author     ：author name
@ version    ：python 3.11
@ Description：
"""
import pytest
from src.doc_generator.pdf_writer import PDFWriter
import pdfkit


def test_write_success(tmp_path, mocker):
    writer = PDFWriter()
    # 模拟 pdfkit.from_string 函数成功执行
    mock_from_string = mocker.patch('src.doc_generator.pdf_writer.pdfkit.from_string')
    # 模拟 find_wkhtmltopdf 方法返回一个路径
    wkhtmltopdf_path = r'D:\program\wkhtmltox\bin\wkhtmltopdf.exe'
    mocker.patch.object(writer, 'find_wkhtmltopdf', return_value=wkhtmltopdf_path)
    content = "<html><body>Test PDF</body></html>"
    output_file = tmp_path / "test_success.pdf"
    writer.write(content, str(output_file))

    # 检查 pdfkit.from_string 是否被正确调用
    mock_from_string.assert_called_once()
    call_args = mock_from_string.call_args

    # 检查位置参数
    assert call_args[0][0] == content
    assert call_args[0][1] == str(output_file)

    # 检查关键字参数
    assert call_args[1]['options'] == {
        'encoding': 'UTF-8',
        'no-outline': None,
        'quiet': '',
    }

    # 检查 configuration 参数
    assert 'configuration' in call_args[1]
    config = call_args[1]['configuration']
    assert hasattr(config, 'wkhtmltopdf')
    assert config.wkhtmltopdf == wkhtmltopdf_path

def test_write_file_creation_failure(tmp_path, mocker, capsys):
    writer = PDFWriter()
    # 模拟 pdfkit.from_string 函数抛出异常
    mocker.patch('src.doc_generator.pdf_writer.pdfkit.from_string',
                 side_effect=Exception("PDF generation failed"))
    content = "<html><body>Test PDF</body></html>"
    output_file = tmp_path / "test_creation_failure.pdf"
    # 我们期望 write 方法会抛出 IOError
    with pytest.raises(IOError) as excinfo:
        writer.write(content, str(output_file))
    # 检查异常信息
    assert "Error generating PDF: PDF generation failed" in str(excinfo.value)
    # 检查是否打印了正确的错误消息到标准错误
    captured = capsys.readouterr()
    assert "Error generating PDF: PDF generation failed" in captured.err