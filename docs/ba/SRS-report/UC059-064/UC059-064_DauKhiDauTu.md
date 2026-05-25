# UC059-064: Báo cáo tình hình thực hiện các dự án hợp tác với nước ngoài trong lĩnh vực dầu khí năm ... (Phụ lục A) — Mẫu A.III.5

| Thuộc tính                          | Giá trị                                                               |
| ------------------------------------- | ----------------------------------------------------------------------- |
| **BA phụ trách**              | quan.trinh                                                              |
| **Phân hệ**                   | Quản lý đầu tư nước ngoài vào Việt Nam                        |
| **Mẫu biểu**                  | Mẫu A.III.5                                                            |
| **Loại báo cáo**             | Định kỳ năm (hạn nộp: trước ngày 31/3 năm sau năm báo cáo) |
| **Hình thức nộp**            | Báo cáo đơn lẻ                                                     |
| **Cơ quan nhận**              | Bộ Tài chính (Cục Đầu tư nước ngoài)                          |
| **Đối tượng lập**          | Tập đoàn Dầu khí Việt Nam (PVN)                                   |
| **Giao diện**                  | Admin site                                                              |
| **Ngày tạo**                  | 2026-04-24                                                              |
| **Phiên bản**                 | 1.8                                                                     |
| **Quy tắc sinh mã báo cáo** | FDI_AIII5_[ID]                                                          |
| **Loại quy trình**           | 3 bước (CMCĐT_BCTK_09)                                                  |

---

## UC059-064.1: Xem Danh Sách Báo Cáo

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Xem danh sách báo cáo tình hình thực hiện các dự án hợp tác với nước ngoài trong lĩnh vực dầu khí năm (Mẫu A.III.5)
- Chức năng cho phép Tập đoàn Dầu khí Việt Nam truy cập danh sách báo cáo định kỳ năm về tình hình thực hiện các dự án hợp tác với nước ngoài, được nhóm theo từng Kỳ hạn báo cáo.

Truy cập chức năng: Phân hệ Báo cáo → Quản lý ĐTNN vào VN → Báo cáo tình hình thực hiện các dự án hợp tác với nước ngoài trong lĩnh vực dầu khí (Mẫu A.III.5)

Chức năng đáp ứng usecase số: 59, 60, 61, 62, 63, 64

---

### 2. Mô tả giao diện

**Giao diện danh sách**

Giao diện:

**Periodic-single**: Giao diện mẫu cho báo cáo có kỳ hạn năm và gửi lẻ từng báo cáo.

Mô tả giao diện:

| #                                                     | Tên trường          | Kiểu trường              | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả                                                                                                                                                                                                                                                    |
| ----------------------------------------------------- | ---------------------- | --------------------------- | --------------------- | ------------ | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Khung Điều kiện Lọc & Tìm kiếm**        |                        |                             |                       |              |            |                                                                                                                                                                                                                                                            |
| 1                                                     | Năm                   | Yearpicker                  | Năm hiện tại       | x            |            | Người dùng nhấp để chọn năm từ calendar picker. Hệ thống lọc và nhóm danh sách theo năm được chọn. Kết quả hiển thị ngay lập tức sau khi chọn, không cần nhấn thêm nút. Tham chiếu: CMR_07.                               |
| 2                                                     | Trạng thái kỳ       | Multiple-selection Dropdown | Null                  | x            |            | Lọc theo trạng thái của kỳ hạn. Người dùng chọn một hoặc nhiều giá trị: Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo. Kết quả lọc hiển thị ngay sau khi chọn. Tham chiếu: CMR_04, CMR_07., CMR_16                                  |
| 3                                                     | Trạng thái báo cáo | Multiple-selection Dropdown | Null                  | x            |            | Lọc theo trạng thái của bản ghi báo cáo. Người dùng chọn một hoặc nhiều giá trị: Lưu nháp / Chờ duyệt / Đã tiếp nhận / Yêu cầu chỉnh sửa. Kết quả lọc hiển thị ngay sau khi chọn. Tham chiếu: CMR_03, CMR_07., CMR_16           |
| 4                                                     | Mã báo cáo          | Search bar                  | Null                  | x            |            | Nhập liệu tự do để tìm theo mã báo cáo. Kết quả hiển thị ngay khi nhập. Nếu không tìm thấy kết quả: hiển thị màn hình trắng với text "Không tìm thấy kết quả". Tham chiếu: CMR_06, CMR_09. Placeholder: "Tìm kiếm nhanh theo mã báo cáo". |
| **Khung Danh sách kỳ hạn**                   |                        |                             |                       |              |            |                                                                                                                                                                                                                                                            |
| 5                                                     | Kỳ hạn báo cáo     | Label                       | Null                  |              |            | Hiển thị tên kỳ hạn. VD: "Năm 2026". Tham chiếu: CMR_08.                                                                                                                                                                                            |
| 6                                                     | Trạng thái kỳ       | Label                       | Null                  |              |            | Hiển thị trạng thái tổng hợp của kỳ: Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo. Tham chiếu: CMR_04.                                                                                                                                  |
| 7                                                     | Lập báo cáo         | Button                      | Null                  |              |            | Chỉ hiển thị khi kỳ ở trạng thái**Trong thời hạn**. Ẩn khi Chưa tới hạn hoặc Qua kỳ báo cáo. Tham chiếu: CF_01, CMR_04.                                                                                                            |
| 8                                                     | Nhập từ file                 | Button                      | Null                  |              |            | Chỉ hiển thị khi kỳ ở trạng thái**Trong thời hạn**. Ẩn khi Chưa tới hạn hoặc Qua kỳ báo cáo. Tham chiếu: CMR_04.                                                                                                                   |
| **Khung Danh sách Báo cáo** (trong mỗi kỳ) |                        |                             |                       |              |            |                                                                                                                                                                                                                                                            |
| 9                                                     | Mã báo cáo          | Label                       | Null                  |              |            | Hiển thị mã báo cáo do hệ thống sinh theo quy tắc. Tham chiếu: CMR_09.                                                                                                                                                                            |
| 10                                                    | Ngày cập nhật       | Label                       | Null                  |              |            | Hiển thị ngày giờ của thao tác gần nhất. Định dạng: dd/MM/yyyy HH:mm.                                                                                                                                                                           |
| 11                                                    | Trạng thái báo cáo | Label                       | Null                  |              |            | Trạng thái cấp bản ghi. Tham chiếu: CMR_03.                                                                                                                                                                                                           |
| 12                                                    | Hành động           | Button group                | Null                  |              |            | Hiển thị các nút thao tác theo trạng thái bản ghi. Chi tiết tham chiếu: UC059-064.3.                                                                                                                                                             |

---

### 3. Mô tả các xử lý của chức năng

- Yêu cầu về hiển thị tại khung danh sách kỳ hạn:
  - Hệ thống tự động nhóm danh sách theo Kỳ hạn báo cáo (năm). Mặc định collapse; click để expand.
  - Thực hiện phân trang cho danh sách kỳ hạn. Tham chiếu: CMR_10.
  - Sắp xếp giảm dần theo thời gian (kỳ mới nhất lên đầu).
- Thao tác lọc & tìm kiếm:
  - Tất cả bộ lọc và ô tìm kiếm đều hiển thị kết quả ngay lập tức, không cần nhấn thêm nút.
  - Nếu không có kết quả: màn hình trắng hiển thị text "Không tìm thấy kết quả".
- Nút [Lập báo cáo] và [Nhập từ file] Chỉ hiển thị khi kỳ ở trạng thái **Trong thời hạn**. Ẩn khi Chưa tới hạn hoặc Qua kỳ báo cáo. Tham chiếu: CMR_04. Tham chiếu: CF_01, CMR_04.

---

## UC059-064.2: Lập Báo Cáo

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Tạo mới báo cáo tình hình thực hiện các dự án hợp tác với nước ngoài trong lĩnh vực dầu khí (Mẫu A.III.5)
- Chức năng cho phép Tập đoàn Dầu khí Việt Nam nhập liệu báo cáo tình hình thực hiện các dự án hợp tác với nước ngoài theo biểu mẫu A.III.5. Báo cáo là eForm Grid cố định số dòng (Fixed Rows), gồm 2 phần song song (Phần I: ĐTVN, Phần II: ĐTNN), mỗi phần 10 chỉ tiêu. Cấu trúc 3 cột: (A) năm trước — auto-fill từ DB, (B) năm báo cáo — nhập tay, (C) So cùng kỳ % — auto-calc. Tham chiếu: CF_01.

Truy cập chức năng: Màn danh sách báo cáo (UC059-064.1) → Nhấn nút [Lập báo cáo]

Chức năng đáp ứng usecase số: 59, 60

---

### 2. Mô tả giao diện

**Giao diện thêm mới**

Giao diện: Màn hình tạo mới theo biểu mẫu A.III.5.

Mô tả giao diện:

| #                                                             | Tên trường                         | Kiểu trường | Giá trị mặc định                | Được sửa           | Bắt buộc                                                                                         | Ghi chú                                                                                                                                                                                                                                                                                              |
| ------------------------------------------------------------- | ------------------------------------- | -------------- | ------------------------------------ | ---------------------- | -------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **PHẦN HEADER**                                        |                                       |                |                                      |                        |                                                                                                    |                                                                                                                                                                                                                                                                                                       |
| 1                                                             | Năm báo cáo                        | Label          | Auto-fill từ Kỳ hạn báo cáo      |                        | x                                                                                                  | Hiển thị năm báo cáo dưới dạng Label (Disabled). Giá trị được xác định tự động từ Kỳ hạn báo cáo đã chọn tại màn hình danh sách (UC059-064.1). Người dùng không thể chỉnh sửa trực tiếp trên form. |
| **PHẦN I — CÁC DỰ ÁN ĐẦU TƯ TẠI VIỆT NAM**    |                                       |                |                                      |                        |                                                                                                    | Group header row. Toàn bộ cột (A), (B), (C) đều Locked. Chỉ hiển thị nhãn.                                                                                                                                                                                                                   |
| 2                                                             | 1.1. Số dự án mới                 | eForm row      | —                                   | x                      | x                                                                                                  | ĐVT: Dự án. Cột (A): Auto-fill từ DB — Editable. Cột (B): Editable, người dùng nhập. Cột (C): Auto-calc = (B/A)*100. Xem RULE-01, RULE-02. Tham chiếu: CMR_05.                                                                                                                           |
| 3                                                             | 1.2. Vốn đầu tư đăng ký mới   | eForm row      | —                                   | x                      | x                                                                                                  | ĐVT: Triệu USD. Cột (A): Auto-fill — Editable. Cột (B): Editable. Cột (C): Auto-calc. Tham chiếu: CMR_05.                                                                                                                                                                                      |
| 4                                                             | 1.3. Số lượt dự án điều chỉnh | eForm row      | —                                   | x                      | x                                                                                                  | ĐVT: Lượt dự án. Cột (A): Auto-fill — Editable. Cột (B): Editable. Cột (C): Auto-calc. Tham chiếu: CMR_05.                                                                                                                                                                                  |
| 5                                                             | 1.4. Vốn đầu tư điều chỉnh     | eForm row      | —                                   | x                      | x                                                                                                  | ĐVT: Triệu USD. Cột (A): Auto-fill — Editable. Cột (B): Editable. Cột (C): Auto-calc. **Cho phép nhập số âm** (trường hợp điều chỉnh giảm vốn). Tham chiếu: CMR_05.                                                                                                                                                                                      |
| 6                                                             | 1.5. Vốn thực hiện                 | eForm row      | —                                   | x                      | x                                                                                                  | ĐVT: Triệu USD. Cột (A): Auto-fill — Editable. Cột (B): Editable. Cột (C): Auto-calc. RULE-03: giá trị dòng cha, dòng con không được vượt quá. Tham chiếu: CMR_05.                                                                                                                  |
| 7                                                             | ↳ Trong đó, từ bên nước ngoài | eForm row      | —                                   | x                      |                                                                                                    | ĐVT: Triệu USD.**Dòng con của 1.5** — UI cần lùi đầu dòng (indent). Cột (A): Auto-fill — Editable. Cột (B): Editable. Cột (C): Auto-calc. RULE-03: giá trị cột (A) và (B) KHÔNG được vượt quá giá trị tương ứng của dòng 1.5. Tham chiếu: CMR_05.              |
| 8                                                             | 1.6. Doanh thu                        | eForm row      | —                                   | x                      | x                                                                                                  | ĐVT: Triệu USD. Cột (A): Auto-fill — Editable. Cột (B): Editable. Cột (C): Auto-calc. Tham chiếu: CMR_05.                                                                                                                                                                                      |
| 9                                                             | 1.7. Xuất khẩu                      | eForm row      | —                                   | x                      | x                                                                                                  | ĐVT: Triệu USD. Cột (A): Auto-fill — Editable. Cột (B): Editable. Cột (C): Auto-calc. Tham chiếu: CMR_05.                                                                                                                                                                                      |
| 10                                                            | 1.8. Nhập khẩu                      | eForm row      | —                                   | x                      | x                                                                                                  | ĐVT: Triệu USD. Cột (A): Auto-fill — Editable. Cột (B): Editable. Cột (C): Auto-calc. Tham chiếu: CMR_05.                                                                                                                                                                                      |
| 11                                                            | 1.9. Lao động                       | eForm row      | —                                   | x                      | x                                                                                                  | ĐVT: Người. **Integer only** — chỉ cho phép số nguyên (chặn ký tự thập phân ngay khi gõ). Cột (A): Auto-fill — Editable. Cột (B): Editable. Cột (C): Auto-calc. Tham chiếu: CMR_05.                                                                                                                                                                                         |
| 12                                                            | 1.10. Nộp ngân sách                | eForm row      | —                                   | x                      | x                                                                                                  | ĐVT: Triệu USD. Cột (A): Auto-fill — Editable. Cột (B): Editable. Cột (C): Auto-calc. Tham chiếu: CMR_05.                                                                                                                                                                                      |
| **PHẦN II — CÁC DỰ ÁN ĐẦU TƯ RA NƯỚC NGOÀI** |                                       |                |                                      |                        |                                                                                                    | Group header row. Toàn bộ cột (A), (B), (C) đều Locked. Chỉ hiển thị nhãn. **Bắt buộc nhập** — tất cả trường trong Phần II đều bắt buộc (có thể điền 0 nếu không có dữ liệu).                                                                                                                   |
| 13                                                            | 2.1. Số dự án mới                 | eForm row      | —                                   | x                      | x                                                                                                  | ĐVT: Dự án. Cấu trúc và logic hoàn toàn tương tự dòng 1.1. Tham chiếu: CMR_05.                                                                                                                                                                                                           |
| 14                                                            | 2.2. Vốn đầu tư đăng ký mới   | eForm row      | —                                   | x                      | x                                                                                                  | ĐVT: Triệu USD. Tương tự 1.2. Tham chiếu: CMR_05.                                                                                                                                                                                                                                               |
| 15                                                            | 2.3. Số lượt dự án điều chỉnh | eForm row      | —                                   | x                      | x                                                                                                  | ĐVT: Lượt dự án. Tương tự 1.3. Tham chiếu: CMR_05.                                                                                                                                                                                                                                           |
| 16                                                            | 2.4. Vốn đầu tư điều chỉnh     | eForm row      | —                                   | x                      | x                                                                                                  | ĐVT: Triệu USD. Tương tự 1.4. **Cho phép nhập số âm** (trường hợp điều chỉnh giảm vốn). Tham chiếu: CMR_05.                                                                                                                                                                                               |
| 17                                                            | 2.5. Vốn thực hiện                 | eForm row      | —                                   | x                      | x                                                                                                  | ĐVT: Triệu USD. Tương tự 1.5. RULE-03. Tham chiếu: CMR_05.                                                                                                                                                                                                                                      |
| 18                                                            | ↳ Trong đó, từ bên nước ngoài | eForm row      | —                                   | x                      |                                                                                                    | ĐVT: Triệu USD. Dòng con của 2.5 — UI indent. RULE-03: không vượt quá 2.5. Tham chiếu: CMR_05.                                                                                                                                                                                              |
| 19                                                            | 2.6. Doanh thu                        | eForm row      | —                                   | x                      | x                                                                                                  | ĐVT: Triệu USD. Tương tự 1.6. Tham chiếu: CMR_05.                                                                                                                                                                                                                                               |
| 20                                                            | 2.7. Xuất khẩu                      | eForm row      | —                                   | x                      | x                                                                                                  | ĐVT: Triệu USD. Tương tự 1.7. Tham chiếu: CMR_05.                                                                                                                                                                                                                                               |
| 21                                                            | 2.8. Nhập khẩu                      | eForm row      | —                                   | x                      | x                                                                                                  | ĐVT: Triệu USD. Tương tự 1.8. Tham chiếu: CMR_05.                                                                                                                                                                                                                                               |
| 22                                                            | 2.9. Lao động                       | eForm row      | —                                   | x                      | x                                                                                                  | ĐVT: Người. **Integer only** — chỉ cho phép số nguyên (chặn ký tự thập phân ngay khi gõ). Tương tự 1.9. Tham chiếu: CMR_05.                                                                                                                                                                                                                                                  |
| 23                                                            | 2.10. Nộp ngân sách                | eForm row      | —                                   | x                      | x                                                                                                  | ĐVT: Triệu USD. Tương tự 1.10. Tham chiếu: CMR_05.                                                                                                                                                                                                                                              |
| **Các Button**                                         |                                       |                |                                      |                        |                                                                                                    |                                                                                                                                                                                                                                                                                                       |
| ---                                                           | ---                                   | ---            | ---                                  | ---                    | ---                                                                                                |                                                                                                                                                                                                                                                                                                       |
|  | Hủy                                  | Button         | Tất cả trạng thái                | Người tạo           | Quay về Danh sách. Popup xác nhận nếu có dữ liệu chưa lưu. Tham chiếu: CF_01.           |                                                                                                                                                                                                                                                                                                       |
|  | Xem trước | Button | Tất cả trạng thái                | Tất cả người dùng | Preview báo cáo (PDF). Tham chiếu: CF_07.1.                                                     |                                                                                                                                                                                                                                                                                                       |
|  | Lưu nháp                            | Button         | Tất cả trạng thái                | Người tạo           | Lưu toàn bộ các Phần ở trạng thái Lưu nháp. Tham chiếu: CF_01.                          |                                                                                                                                                                                                                                                                                                       |
|  | Nộp báo cáo                        | Button         | Lưu nháp và Yêu cầu chỉnh sửa | Người tạo           | Validate toàn bộ trường bắt buộc và logic cross-field trước khi nộp. Tham chiếu: CF_01. |                                                                                                                                                                                                                                                                                                       |

---

### 3. Mô tả các xử lý của chức năng

**Xử lý chung:** Tham chiếu: CF_01 (Lập báo cáo), CMR_18, CF_04 (Xuất báo cáo), CF_05 (In).

**Xử lý đặc thù Mẫu A.III.5:**

- **Khởi tạo form:** Hệ thống tự động load dữ liệu cột (A) từ cơ sở dữ liệu — lấy giá trị cột (B) của báo cáo năm T-1 (năm liền trước năm báo cáo hiện tại) đã được phê duyệt thành công. Tham chiếu: RULE-01.
- **Trigger auto-fill cột (A):**
  - **Khi form load:** Hệ thống auto-fill cột (A) dựa vào giá trị **Năm báo cáo** (được xác định từ Kỳ hạn báo cáo đã chọn tại màn hình danh sách). Năm báo cáo là Label/Disabled nên không có trigger thay đổi năm trên form.
- **RULE-01 — Auto-fill cột (A):**

  - Nếu tìm thấy dữ liệu năm T-1: điền sẵn vào cột (A). Cột (A) vẫn là Editable để người dùng có thể chỉnh sửa trong trường hợp có thay đổi kiểm toán hoặc sai sót số dư đầu kỳ.
  - Nếu không tìm thấy dữ liệu (dự án mới hoặc chưa có báo cáo T-1): cột (A) hiển thị trống và Editable để người dùng tự nhập số liệu lịch sử.
- **RULE-02 — Xử lý chia cho không tại cột (C):**

  - Cột (C) = (Cột B / Cột A) × 100.
  - Nếu Cột (A) = 0 hoặc NULL (bỏ trống): cột (C) tự động hiển thị "N/A" thay vì thực hiện phép tính. Không phát sinh lỗi NaN hay Infinity.
  - Cột (C) cập nhật real-time khi người dùng thay đổi cột (A) hoặc (B).
- **RULE-03 — Validate dòng con ≤ dòng cha (Vốn thực hiện):**

  - Tại mục 1.5 (và 2.5): dòng con "Trong đó, từ bên nước ngoài" không được lớn hơn dòng cha "Vốn thực hiện" — áp dụng cho cả cột (A) lẫn cột (B).
  - Validate on-blur: ngay khi người dùng rời khỏi ô, hệ thống kiểm tra và hiển thị viền đỏ inline kèm error text: *"Giá trị không được vượt quá dòng cha"* nếu vi phạm.
  - Validate khi Nộp: nếu vi phạm → dừng luồng, hiển thị Toast lỗi: "Số vốn nước ngoài không được vượt quá Tổng vốn thực hiện". Tham chiếu: CF_01.
- **Validate khi Nộp:** Kiểm tra tất cả trường Bắt buộc trong cột (B) đã có giá trị. Các trường dòng con "Trong đó, từ bên nước ngoài" là Optional (không bắt buộc). Phần II bắt buộc nhập — có thể điền 0 nếu không có dữ liệu.
- **Validation Số âm:** Mục 1.4 và 2.4 (Vốn đầu tư điều chỉnh) cho phép nhập số âm (trường hợp điều chỉnh giảm vốn). Tất cả các mục còn lại chỉ cho phép số >= 0.
- **API/Data Failure:** Trường hợp không load được dữ liệu Cột (A) do lỗi hệ thống → hiện Toast **T05** và cho phép nhập tay. Tham chiếu: **CMR_12**.
- Xuất báo cáo: Kết xuất file **Excel**. **Chỉ từ Màn hình danh sách** (không có trong Preview). Nếu bản ghi có thay đổi chưa Lưu → popup cảnh báo. Tham chiếu: CF_04.

---

## UC059-064.3: Các Tác Vụ Bổ Trợ

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Các tác vụ bổ trợ — Xem chi tiết, Xem vòng đời, In, Kết xuất, Nộp, Chỉnh sửa
- Chức năng cho phép người dùng thực hiện các tác vụ bổ trợ tương ứng trạng thái bản ghi.

Truy cập chức năng: Màn danh sách báo cáo (UC059-064.1) → Cột Hành động → Chọn tác vụ tương ứng

Chức năng đáp ứng usecase số: 61, 62, 63, 64

---

### 2. Mô tả giao diện

**Các Button theo Action Mapping:**

| # | Tên            | Kiểu  | Điều kiện hiển thị                   | Mô tả                                                                          |
| - | --------------- | ------ | ----------------------------------------- | -------------------------------------------------------------------------------- |
| 1 | Nộp            | Button | Chỉ Lưu nháp và Yêu cầu chỉnh sửa | Tham chiếu: CF_09. Tham chiếu: CF_01 (mục "Xử lý nút [Nộp báo cáo]").   |
| 2 | Chỉnh sửa     | Button | Chỉ Lưu nháp và Yêu cầu chỉnh sửa | Tham chiếu: CF_03.                                                              |
| 3 | Xem chi tiết   | Button | Tất cả trạng thái                     | Điều hướng đến màn hình Xem toàn trang (full-page). Tham chiếu: CF_07. |
| 4 | Xem vòng đời | Button | Tất cả trạng thái                     | Tham chiếu: CF_06.                                                              |
| 5 | In              | Button | Tất cả trạng thái                     | Tham chiếu: CF_05.                                                              |
| 6 | Xuất báo cáo          | Button | Tất cả trạng thái                     | Kết xuất file Excel. **Chỉ từ Màn hình danh sách** (không có trong Preview). Nếu bản ghi có thay đổi chưa Lưu → hiển thị popup: *"Nội dung xuất file là bản đã lưu gần nhất. Vui lòng Lưu nháp trước khi xuất nếu muốn cập nhật."* Tham chiếu: CF_04.                                       |
| 7 | Xóa            | Button | Lưu nháp**VÀ** chưa từng nộp  | Tham chiếu: CF_08.                                                              |

---

### 3. Mô tả các xử lý của chức năng

- Xem chi tiết (màn hình View full-page): Tham chiếu: CF_07.
- Xem vòng đời: Tham chiếu: CF_06.
- In báo cáo: Tham chiếu: CF_05.
- Xuất báo cáo: Kết xuất ra file **Excel**. **Chỉ từ Màn hình danh sách** (không có trong Preview). Nếu bản ghi có thay đổi chưa Lưu → popup cảnh báo. Tham chiếu: CF_04.
- Chỉnh sửa báo cáo: Tham chiếu: CF_03.

---

## 4. Lịch sử cập nhật

| Ngày      | Phiên bản | Mục cập nhật                          | Before                                               | After                                                                        | Ghi chú                                                    |
| ---------- | ----------- | ---------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------------------------------- | ----------------------------------------------------------- |
| 2026-05-05 | 1.0 → 1.1  | UC059-064.2 trường #2–#23 (eForm row) | Không có tham chiếu CMR_05                        | Bổ sung Tham chiếu: CMR_05 cho tất cả 22 dòng eForm row nhập số       | Đồng bộ quy tắc trường số với CMR_05                |
| 2026-05-08 | 1.1 → 1.2  | Audit chuyên sâu & UX update           | v1.1 - Thiếu nút [Xem chi tiết], sai Toast "Quý" | Thêm nút B25, chuẩn hóa Toast V17 (Năm), thêm Toast T05 và sync CF_01 | Đồng bộ toàn hệ thống                                 |
| 2026-05-11 | 1.0→1.1    | Quy tắc sinh mã báo cáo              | `DTNN_A3_5_[ID]`                                   | `FDI_AIII5_[ID]`                                                           | Chuẩn hóa prefix và mã theo appendices.md v2.0 (INS-10) |
| 2026-05-11 | +1          | Tên cột                                | `Ngày cập nhật / Nộp`                          | `Ngày cập nhật`                                                         | Đồng bộ tên cột theo CS_02 (INS-03)                    |
| 2026-05-11 | +1          | Label Trạng thái kỳ                   | `Trạng thái (cấp kỳ)`                          | `Trạng thái kỳ`                                                         | Chuẩn hóa tên label (INS-06)                             |
| 2026-05-11 | +1          | Kiểu field Năm báo cáo               | `Number`                                           | `Yearpicker`                                                               | Đồng nhất kiểu field (INS-04)                           |
| 2026-05-11 | +1          | Phân quyền UC059-064.1 & .2            | `Tham chiếu: CMR_02`                              | `Chỉ Tập đoàn Dầu khí Việt Nam (PVN)`                               | Xóa CMR_02, ghi inline theo quyết định BA (INS-01)      |
| 2026-05-11 | +1          | Phân quyền UC059-064.3                 | `CMR_02, CMR_03`                                   | `CMR_03`                                                                   | Xóa CMR_02 dư thừa (INS-01)                              |
| 2026-05-11 | +1          | Dòng phân cách bảng Markdown         | Thiếu cột (1 chỗ)                                 | Đủ số cột theo header                                                    | Chuẩn hóa separator (INS-05)                              |
| 2026-05-12 | 1.2 → 1.3 | PHẦN HEADER — #1 Năm báo cáo — Validate min year | Danh sách năm ≤ hiện tại | Danh sách năm **từ 1987** đến hiện tại. Validate min: ≥ 1987. Lỗi: *"Năm báo cáo không được nhỏ hơn 1987."* | Chuẩn hóa mốc năm 1987 theo quy định hệ thống |
| 2026-05-13 | 1.3 → 1.4 | Mục 3 — Trigger auto-fill cột (A) | Chỉ mô tả "Khởi tạo form: auto-fill cột (A) từ DB" (không nêu rõ thời điểm trigger) | Bổ sung: (1) Khi form load → auto-fill theo Năm báo cáo default; (2) Khi người dùng đổi Năm báo cáo → cập nhật real-time, ghi đè trực tiếp không popup | Làm rõ behavior trigger theo yêu cầu BA |
| 2026-05-14 | 1.4 → 1.5  | UC059-064.1 Mục 3 — Column Sort | (Không có) | Bổ sung: Cột Ngày/Số hiển thị icon Sort trên header. Single-column sort. Client-side | Chuẩn hóa UX sort toàn hệ thống |
| 2026-05-14 | 1.4 → 1.5  | UC059-064.2 Mục 3 — Decimal precision | (Không có) | Bổ sung: Phần thập phân tối đa 5 chữ số, auto-round half-up khi blur | Chuẩn hóa precision toàn hệ thống |
| 2026-05-14 | 1.4 → 1.5  | UC059-064.2 Mục 3 — Max length mặc định | (Không có) | Bổ sung: Textbox 500, Textarea 2000, Number 20, Search 200 ký tự | Chuẩn hóa validation rules toàn hệ thống |
| 2026-05-14 | 1.5 → 1.6  | #5 (1.4) Vốn đầu tư điều chỉnh — Cho phép số âm | Không quy định cho phép số âm | Bổ sung: Cho phép nhập số âm (trường hợp điều chỉnh giảm vốn) | Yêu cầu nghiệp vụ |
| 2026-05-14 | 1.5 → 1.6  | Phần II — Bắt buộc nhập | Không ghi rõ bắt buộc | Bổ sung: Tất cả trường Phần II bắt buộc nhập, có thể điền 0 nếu không có dữ liệu | Yêu cầu nghiệp vụ |
| 2026-05-14 | 1.5 → 1.6  | #16 (2.4) Vốn đầu tư điều chỉnh — Cho phép số âm | "Tương tự 1.4" (không ghi rõ số âm) | Bổ sung: Cho phép nhập số âm (trường hợp điều chỉnh giảm vốn) | Yêu cầu nghiệp vụ |
| 2026-05-17 | CMR v2.0 | Placeholder Search bar (1 dong) | Nhap du lieu | Tim kiem nhanh theo ma bao cao | Chuan hoa CMR_06 v2.0 STD-04b |
| 2026-05-17 | CMR v2.0 | Them tham chieu CMR_16 (2 dong filter dropdown) | Chua co CMR_16 | Them , CMR_16 sau CMR_07 tren cac dong Multiple-selection Dropdown | Filter dropdown phai co option Tat ca (CMR_16) |
| 2026-05-17 | CMR v2.0 | Them tham chieu CMR_18 (Tab Navigation) | Chua co CMR_18 | Them , CMR_18 vao tham chieu CF_01 tren man hinh lap bao cao | Tuan thu CMR_18 Tab Navigation (STD-07) |
| 2026-05-18 | CMR v2.0 -> 2.1 | Thuật ngữ nút bấm | Export / Import | Xuất báo cáo / Nhập từ file | Cập nhật đồng bộ tiếng Việt |
| 2026-05-18 | 1.6 → 1.7 | #1 Năm báo cáo — Kiểu trường | Yearpicker / Editable | Label / Disabled — auto-fill từ Kỳ hạn báo cáo đã chọn tại danh sách | Năm xác định từ màn hình danh sách, không cho sửa trên form |
| 2026-05-18 | 1.6 → 1.7 | Mục 3 — Trigger auto-fill cột (A) | (1) form load + (2) khi đổi Năm báo cáo | Chỉ giữ (1) form load. Xóa trigger (2) vì Năm là Label/Disabled | Năm không thể thay đổi trên form |
| 2026-05-18 | 1.6 → 1.7 | Mục 3 — Check trùng kỳ V17 | Check khi Lưu/Nộp, lỗi inline V17 | Xóa hoàn toàn — hệ thống kiểm soát trùng kỳ tại màn hình danh sách | Không cần validate trùng kỳ trên form |
| 2026-05-18 | 1.6 → 1.7 | Mục 3 — RULE-03 on-blur | Viền đỏ inline (không có error text) | Viền đỏ inline kèm error text: *"Giá trị không được vượt quá dòng cha"* | Bổ sung inline error message cho QA verify |
| 2026-05-18 | 1.6 → 1.7 | #11 (1.9) và #22 (2.9) Lao động | ĐVT: Người (không quy định integer/decimal) | Integer only — chặn ký tự thập phân ngay khi gõ | ĐVT Người = số nguyên, block decimal tại keystroke |
| 2026-05-19 | 1.7 → 1.8 | UC059-064.1 Mục 3 — Xóa Column Sort | Bổ sung: Cột Ngày/Số hiển thị icon Sort trên header. Single-column sort. Client-side | (Đã xóa) — thông tin sai, không có yêu cầu từ BA | Xóa đặc tả Column Sort khỏi SRS |
| 2026-05-19 | 1.7 → 1.8 | UC059-064.2 Mục 3 — Xóa Decimal precision + Max length | Decimal precision auto-round 5 chữ số + Max length Textbox 500/Textarea 2000/Number 20/Search 200 | (Đã xóa) — tuân thủ CMR_05 v2.0 "Không cắt thập phân" + Numeric max 18, Text max 500 | Xóa rule ghi đè CMR_05/CMR_06 |
| 2026-05-22 | 1.7 → 1.8 | Phân quyền (UC059-064.1, .3) + Action Mapping cột Phân quyền | Nội dung phân quyền inline + cột Phân quyền trong bảng Action Mapping | (Đã xóa) | Lược bỏ nội dung phân quyền theo yêu cầu tách riêng |
