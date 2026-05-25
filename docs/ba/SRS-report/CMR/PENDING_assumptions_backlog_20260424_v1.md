# ASSUMPTIONS BACKLOG — Chờ xác nhận

> Ngày tạo: 2026-04-24
> Mục đích: Tổng hợp toàn bộ câu hỏi assumption đang chờ xác nhận từ các UC pending. Sau khi BA trả lời, SRS tương ứng sẽ được viết ngay.

---

## UC125-130 — Mẫu A.IV.9a

**Báo cáo tổng hợp tình hình tài chính và nộp ngân sách của TCKT có vốn ĐTNN năm (theo địa bàn tỉnh/thành phố)**

- Đối tượng lập: Cục Thuế / Bộ Tài chính
- Đặc thù: Bảng theo địa bàn 63 tỉnh/TP

| ID   | Câu hỏi                                                                                                                                                                  | Trả lời                                                                                         |
| ---- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| A-01 | Bảng dữ liệu có**cố định 63 dòng** tương ứng 63 tỉnh/thành phố (không thêm/xóa dòng), hay cho phép thêm động?                                  | k cố định đâu, tỉnh nào có số thì mới lên báo cáo thôi                             |
| A-02 | Dữ liệu các cột số liệu có được**auto-fill từ API Cục Thuế** không, hay toàn bộ nhập tay?                                                           | Note theo dạng này nhé, k có API thì thôi cứ nhập tay còn có thì khả năng như này: |
| A-03 | Nếu có auto-fill từ API: các ô auto-fill có**vẫn Editable** để cán bộ hiệu chỉnh không (giống pattern đã áp dụng ở các UC tài chính trước)? | auto-fill nhưng editable nhé note kỹ vào nha vì cái này khác CMR                          |

A-02Note khả năng tích hợp API vs Cục Thuế:

+ Nguồn API: Lấy từ kho dữ liệu Báo cáo Tài chính và Hồ sơ nộp thuế của Hệ thống quản lý Thuế (TMS).
+ Cơ chế Auto-fill:
  -> API rà quét toàn bộ Doanh nghiệp có Mã số thuế thuộc diện FDI.
  -> Gom nhóm (Group By) các công ty theo trường Tỉnh/Thành phố.
  -> Quét dòng doanh thu/lợi nhuận: Đếm (Count) số công ty nào Lợi nhuận < 0 thì nhét vào cột "Lỗ", Công ty nào Lợi nhuận > 0 thì nhét vào cột "Lãi".
  -> Quét biên lai nộp thuế của các công ty đó trong năm: Phân loại theo mã tiểu mục thu NSNN để dồn tổng tiền (Sum) vào 3 ô: Thu XNK, Thu nội địa, Thu từ dầu thô. (Lưu ý phải chia cho 1.000.000 vì đơn vị ở form định dạng là triệu VNĐ).

---

## UC137-142 — Mẫu A.IV.10a

**Báo cáo tổng hợp tình hình lao động nước ngoài làm việc tại các TCKT có vốn ĐTNN năm (theo quốc tịch)**

- Đối tượng lập: Bộ Nội vụ (Cục Việc làm)

| ID   | Câu hỏi                                                                                                                                                                                                             | Trả lời                                                     |
| ---- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| A-01 | Đối tượng lập ghi là**Bộ Nội vụ (Cục Việc làm)** — xác nhận đây là đúng, không phải Bộ LĐ-TB&XH?                                                                                        | ừ bộ nội vụ                                               |
| A-02 | Cấu trúc bảng: dữ liệu theo**từng quốc tịch** — bảng có **cố định** số dòng (danh sách quốc gia từ master data) hay **lặp động** (người dùng tự thêm dòng quốc tịch)? | lập động,                                                  |
| A-03 | Có API nào tự động đẩy dữ liệu vào báo cáo không, hay toàn bộ nhập tay thủ công?                                                                                                                    | cũng có khả năng nhưng không có thì nhập tay thôi  |

*Note khả năng tích hợp API với BỘ NỘI VỤ
Giao diện sẽ chuyển sang trạng thái tự động 100% (Read-only). Cơ chế xử lý các thông tin tự điền như sau:

+ Nguồn API: Lấy dữ liệu trực tiếp từ Hệ thống cấp Giấy phép lao động (Work Permit) điện tử của Cục Việc Làm.
+ Dữ liệu API mang về: Danh sách toàn bộ lao động nước ngoài có giấy phép đang còn hiệu lực tính đến ngày báo cáo. Kèm theo Mã số thuế của doanh nghiệp họ đang làm việc.
  -> Logic Mapping (Cơ chế xử lý tự điền vào Form):
  Bước 1: Hệ thống đối chiếu Mã số thuế đó với Danh sách Doanh nghiệp FDI lưu trong Cổng đầu tư để lọc ra đúng đối tượng.
  Bước 2: Gom nhóm (Group By) toàn bộ số nhân sự thu được theo đúng tiêu chí "Quốc tịch" (Ví dụ: tách riêng ông Mỹ, ông Hàn, ông Nhật...).
  Bước 3: Đếm số lượng cụ thể và tự động đâm ra N dòng tương ứng trên Grid lưới báo cáo.

- Quốc tịch: Loại Input: Text/Dropdown. Validation: Bắt buộc, phải thuộc đúng danh mục Quốc gia/Quốc tịch chuẩn quốc tế (Master Data Quốc gia ISO), không trùng lặp dòng.

---

## UC143-148 — Mẫu A.IV.10b

**Báo cáo tổng hợp tình hình lao động nước ngoài làm việc tại các TCKT có vốn ĐTNN năm (theo địa bàn tỉnh/thành phố)**

- Đối tượng lập: Bộ LĐ-TB&XH (Cục Việc làm)
- Đặc thù: Bảng theo địa bàn

| ID   | Câu hỏi                                                                                                                                               | Trả lời               |
| ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| A-01 | Bảng dữ liệu có**cố định 63 dòng** (63 tỉnh/TP) không thêm/xóa, hay lặp động?                                                      | không cố định đâu |
| A-02 | Danh sách filter trên màn hình danh sách có bao gồm filter**Địa bàn** không (ngoài Năm / Trạng thái kỳ / Trạng thái báo cáo)? | bỏ địa bàn đi      |
| A-03 | Có API nào cấp dữ liệu tự động không, hay toàn bộ nhập tay?                                                                                 |                         |

*Note khả năng tích hợp API với Bộ LĐTBXH (Cục Việc làm) (do họ cấp Giấy phép lao động Work Permit).

- Hệ thống có thể gọi API chéo để Auto-fill 100% cột "Tổng số lao động ở thời điểm báo cáo".
  -> Logic Mapping: Count tổng số lượng Giấy phép lao động cấp cho người nước ngoài (Work Permits) đang còn hiệu lực tính đến ngày 31/12 của năm báo cáo.
  -> Query chéo với "Mã số thuế doanh nghiệp" bên Tổng cục Thuế để xác định Công ty đó là FDI.
  -> nhóm lại (Group By) theo "Tỉnh/Thành phố" trả về cho 63 dòng.
  -> Khi đó, báo cáo này sẽ Disable toàn bộ khung nhập liệu, User từ Bộ LĐTBXH chỉ việc nhấn "Xác nhận & Nộp".

---

## UC149-154 — Mẫu A.IV.11

**Báo cáo tổng hợp tình hình chuyển giao công nghệ tại TCKT có vốn ĐTNN năm (theo địa bàn tỉnh/thành phố)**

- Đối tượng lập: Bộ Khoa học và Công nghệ

| ID   | Câu hỏi                                                                                                                                                                                                                                        | Trả lời    |
| ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------ |
| A-01 | Chế độ**không có API** (nhập tay thuần): các cột dữ liệu C3–C10 đều Enabled để nhập tay, bảng cố định 63 dòng địa bàn?                                                                                            | k cố định |
| A-02 | Khi**API Bộ KH&CN** điền dữ liệu: các ô C3–C10 sau khi auto-fill có vẫn **Enabled** để người dùng hiệu chỉnh không (giống pattern các UC trước đã áp dụng)?                                                | ok           |
| A-03 | **Cross-field validation:** Khi người dùng nhập `Số lượng = 0` → hệ thống tự động set `Giá trị = 0` và **Disabled** ô Giá trị. Khi `Số lượng > 0` → Giá trị trở lại Enabled. Xác nhận logic này? | ok           |

---

> **Hướng dẫn trả lời:** Điền câu trả lời vào cột "Trả lời" cho từng assumption. Sau khi BA xác nhận, SRS tương ứng sẽ được tạo ngay.

---

## UC364-366 — Quản lý báo cáo đã nộp của tôi

**Nhóm chức năng:** Xem danh sách + Lọc / Xem chi tiết / Chỉnh sửa báo cáo đã nộp

| ID | Câu hỏi | Trả lời |
| --- | --- | --- |
| A-01 | Màn hình "Báo cáo đã nộp của tôi" chỉ hiển thị báo cáo do chính user nộp, hay bao gồm cả báo cáo do NĐT/TCKT khác nộp mà user có quyền xem? (Assumption: Chỉ hiển thị báo cáo do chính user nộp — dựa trên tên "của tôi") | Hiển thị cả báo cáo mà NĐT liên quan trong TCKT hoặc dự án có thể thấy. Refer CS_01 Mục 5. Tooltip hiển thị nguồn gốc báo cáo. |
| A-02 | Xem chi tiết (UC-364-366.2): Xác nhận là full-page read-only (không phải popup CF_07)? (Assumption: Full-page read-only — dựa trên input ghi rõ "full-page, read-only") | Chốt: Nút từ danh sách dẫn đến View Detail Screen (full-page). Popup PDF Preview chỉ kích hoạt từ bên trong View Detail/Lập/Chỉnh sửa qua nút [Preview]. |
| A-03 | Summary Cards: "Số cố định" = không thay đổi khi filter, nhưng có tính lại khi reload trang không? (Assumption: Có — tính lại từ API khi load trang) | Ý "cố định" = disabled (auto-count dựa trên dữ liệu bảng thực tế). Có 5 cards (1 tổng + 4 trạng thái). |
| A-04 | Dropdown page size (10/20/50/100) có cần cho màn hình này không? (Assumption: Không — fix cứng 10/trang theo input) | Có — dropdown với options 10/20/50/100. Đã cập nhật CMR_10. |
| A-05 | Kỳ báo cáo hiển thị format gì? VD: "Kỳ I năm 2026", "Quý 1/2026"? (Assumption: Hiển thị đúng format kỳ hạn tương ứng loại báo cáo — "6 tháng đầu năm 2026", "Quý 1/2026", "Năm 2026") | Phụ thuộc loại BC: Năm → "Năm 2026"; Quý → "Quý 1 năm 2026"; Tháng → "Tháng 2 năm 2026"; 6 tháng → "Kỳ I năm 2026". |
| A-06 | Với ĐTRNN (CMR_02), khi báo cáo ở "YC chỉnh sửa": Tất cả NĐT đều thấy [Chỉnh sửa] hay chỉ NĐT đã nộp? (Assumption: Tất cả NĐT đều thấy — theo CMR_02 + CF_03 quy định rõ) | Đúng. Tất cả NĐT kể cả lập hay không lập đều có quyền chỉnh sửa với trạng thái Lưu nháp/YC chỉnh sửa. Last Write Wins (CMR_02). |
| A-07 | Nút [Xem vòng đời] có bổ sung vào cột Thao tác không? CMR_03 yêu cầu. (Assumption: Có — bổ sung icon cho tất cả trạng thái, tham chiếu CF_06) | Có — thêm button này vào doc. |

---

## UC107-112 — Mẫu A.IV.8a

**Báo cáo tổng hợp tình hình xuất, nhập khẩu của TCKT có vốn ĐTNN năm (Phụ lục A)**

- Đối tượng lập: Cục Hải quan, Bộ Tài chính
- Đặc thù: Aggregation từ Mẫu 8b (xuất khẩu) + Mẫu 8c (nhập khẩu)

| ID | Câu hỏi | Trả lời |
| --- | --- | --- |
| A-01 | Implementation Plan ban đầu giả định bảng cố định 63 dòng (63 tỉnh/TP). BA comment **"Không cố định"** — vậy bảng theo cơ chế nào? Lặp động (user tự thêm dòng tỉnh)? Hay load theo dữ liệu 8b/8c (tỉnh nào có dữ liệu aggregate mới hiện)? | |
| A-02 | Khi bảng không cố định: tỉnh nào không có dữ liệu từ 8b/8c → dòng đó có hiển thị không (giá trị = 0) hay ẩn hoàn toàn? | |
| A-03 | Người dùng có thể tự thêm dòng mới (thêm tỉnh) ngoài kết quả aggregate không, hay chỉ hiển thị đúng những tỉnh có dữ liệu? | |

---

## UC367-372 — Quản lý báo cáo NĐT/Địa phương nộp (Admin side)

**Tính năng quản lý và xử lý báo cáo đã được NĐT/Địa phương nộp — phía Admin (Cán bộ chuyên môn / Lãnh đạo Cục ĐTNN)**

| ID | Câu hỏi | Trả lời |
| --- | --- | --- |
| A-01 | Trạng thái "Đang xử lý" ở phía Admin tương đương trạng thái "Chờ duyệt" ở phía NĐT (CMR_03)? Assumption: Đúng — cùng 1 bản ghi, khác label theo góc nhìn. | |
| A-02 | "Từ chối" là trạng thái cuối (final state) — NĐT không thể nộp lại sau khi bị từ chối? Assumption: Đúng, final state. | |
| A-03 | Admin có thể thực hiện YCCS/Phê duyệt/Từ chối trên báo cáo đang ở trạng thái "YCCS" (ngoài "Đang xử lý")? Assumption: Có — theo mockup, buttons hiển thị cho cả ĐXL và YCCS. | |
| A-04 | Khi Admin YCCS lần 2 (báo cáo đã ở trạng thái YCCS), trạng thái giữ nguyên "YCCS" và NĐT nhận thông báo mới? Assumption: Đúng. | |
| A-05 | Email notification template cho các hành động (Phê duyệt/Từ chối/YCCS) chưa được thiết kế — ghi nhận pending. Assumption: Hệ thống gửi thông báo in-app + email với nội dung cơ bản. | |
| A-06 | Filter "Ngày nộp" là Dropdown chọn khoảng thời gian (không phải Datepicker)? Assumption: Dropdown với các giá trị preset (7 ngày, 30 ngày, Quý, Năm). | |
| A-07 | nút [Xuất báo cáo] trên danh sách và chi tiết đều tuân theo CF_04 (xuất file .docx/.xlsx theo biểu mẫu)? Assumption: Đúng. | |

