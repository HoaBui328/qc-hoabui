# UC227-231: Báo cáo tình hình thực hiện dự án đầu tư năm ... (Mẫu A.III.2)

| Thuộc tính                            | Giá trị                                                               |
| --------------------------------------- | ----------------------------------------------------------------------- |
| **BA phụ trách**                | quan.trinh                                                              |
| **Phân hệ**                     | Quản lý đầu tư trong nước Việt Nam                        |
| **Mẫu biểu**                    | Mẫu A.III.2 2026.4.20 Phu luc A.III-IV                                 |
| **Loại báo cáo**               | Định kỳ năm (hạn nộp: trước 31/3 năm sau)                      |
| **Hình thức nộp**              | Báo cáo đơn lẻ theo từng dự án                                  |
| **Cơ quan nhận**                | Cơ quan đăng ký đầu tư + Cơ quan thống kê tại địa phương |
| **Đối tượng lập**            | Tổ chức kinh tế (TCKT) thực hiện dự án                           |
| **Giao diện**                    | User site                                                               |
| **Ngày tạo**                    | 2026-05-21                                                              |
| **Phiên bản**                   | 1.3                                                                     |
| **Quy tắc sinh mã báo cáo**   | DDI_AIII2_[ID]                                                          |
| **Loại quy trình**             | 2 bước (CMCĐT_BCTK_02, CMCĐT_BCTK_03)                                 |
| **Phạm vi dữ liệu đầu vào** | Có (chọn dự án)                                                     |

> **Lưu ý kiến trúc:** Báo cáo này do Tổ chức kinh tế thực hiện dự án lập. Mỗi báo cáo gắn với 1 dự án cụ thể. Cấu trúc gồm 3 phần: Phần A (Form thông tin chung), Phần B (eForm grid 2 cột dữ liệu), Phần C (Textarea tự do).

---

## UC227-231.1: Xem Danh Sách Báo Cáo

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Xem danh sách báo cáo tình hình thực hiện dự án đầu tư năm (Mẫu A.III.2)
- Chức năng cho phép Tổ chức kinh tế truy cập danh sách báo cáo định kỳ năm theo từng dự án, được nhóm theo Kỳ hạn báo cáo. Mỗi TCKT chỉ thấy báo cáo do mình lập.

Truy cập chức năng: Phân hệ Báo cáo → Quản lý đầu tư trong nước Việt Nam → Báo cáo tình hình thực hiện dự án đầu tư năm (Mẫu A.III.2)

Chức năng đáp ứng usecase số: 227, 228, 229, 230, 231

---

### 2. Mô tả giao diện

Giao diện: **Periodic-single** — Báo cáo có kỳ hạn năm, gửi lẻ từng dự án.

| #                                                     | Tên trường          | Kiểu trường              | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả                                                                                                                                                                                          |
| ----------------------------------------------------- | ---------------------- | --------------------------- | --------------------- | ------------ | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Khung Điều kiện Lọc & Tìm kiếm**        |                        |                             |                       |              |            |                                                                                                                                                                                                  |
| 1                                                     | Năm                   | Yearpicker                  | Năm hiện tại       | x            |            | Chọn năm; hệ thống lọc và nhóm danh sách theo năm. Kết quả hiển thị ngay. Tham chiếu: CMR_07.                                                                                      |
| 2                                                     | Trạng thái kỳ       | Multiple-selection Dropdown | Null                  | x            |            | Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo. Tham chiếu: CMR_04, CMR_07, CMR_16                                                                                                             |
| 3                                                     | Dự án                | Dropdown/Search             | Tất cả dự án | x            |            | Lọc theo dự án cụ thể. Danh sách chỉ hiển thị dự án thuộc TCKT đang đăng nhập. Tham chiếu: **CMR_01**, CMR_16. |
| 4                                                     | Trạng thái báo cáo | Multiple-selection Dropdown | Null                  | x            |            | Người dùng chọn một hoặc nhiều giá trị: Lưu nháp / Chờ duyệt / Đã tiếp nhận / Yêu cầu chỉnh sửa. Kết quả lọc hiển thị ngay sau khi chọn. Tham chiếu: CMR_03, CMR_07, CMR_16 |
| 5                                                     | Mã báo cáo          | Search bar                  | Null                  | x            |            | Tìm theo mã báo cáo. Tham chiếu: CMR_06, CMR_09. Placeholder: "Tìm kiếm nhanh theo mã báo cáo".                                                                                                            |
| **Khung Danh sách Kỳ hạn**                   |                        |                             |                       |              |            |                                                                                                                                                                                                  |
| 6                                                     | Kỳ hạn báo cáo     | Label                       | Null                  |              |            | VD: "Năm 2026". Mặc định collapse; click expand. Tham chiếu: CMR_08.                                                                                                                        |
| 7                                                     | Trạng thái kỳ       | Label                       | Null                  |              |            | Tham chiếu: CMR_04.                                                                                                                                                                             |
| 8                                                     | Lập báo cáo         | Button                      | Null                  |              |            | Chỉ hiển thị khi Trong thời hạn. Ẩn khi Chưa tới hạn hoặc Qua kỳ báo cáo. Tham chiếu: CF_01, CMR_18.                                                                                       |
| 9                                                     | Nhập từ file                 | Button                      | Null                  |              |            | Chỉ hiển thị khi Trong thời hạn. Ẩn khi Chưa tới hạn hoặc Qua kỳ báo cáo.                                                                                                           |
| **Khung Danh sách Báo cáo** (trong mỗi kỳ) |                        |                             |                       |              |            |                                                                                                                                                                                                  |
| 10                                                    | Tên dự án           | Label                       | Null                  |              |            | Hiển thị tên dự án gắn với báo cáo (giá trị A-001).                                                                                                                                   |
| 11                                                    | Mã báo cáo          | Label                       | Null                  |              |            | Mã do hệ thống sinh. Tham chiếu: CMR_09.                                                                                                                                                     |
| 12                                                    | Ngày cập nhật       | Label                       | Null                  |              |            | Định dạng: dd/MM/yyyy HH:mm.                                                                                                                                                                  |
| 13                                                    | Trạng thái báo cáo | Label                       | Null                  |              |            | Tham chiếu: CMR_03.                                                                                                                                                                             |
| 14                                                    | Hành động           | Button group                | Null                  |              |            | Chi tiết tham chiếu: UC227-231.3.                                                                                                                                                              |

---

### 3. Mô tả các xử lý của chức năng

- Hệ thống nhóm danh sách theo Kỳ hạn (năm), mặc định collapse. Sắp xếp giảm dần.
- Nút [Lập báo cáo] và [Nhập từ file] Chỉ hiển thị khi Trong thời hạn. Ẩn khi Chưa tới hạn hoặc Qua kỳ báo cáo. Tham chiếu: CF_01, CMR_18.
- Khi kỳ hạn ở trạng thái Chưa tới hạn, hiển thị Empty state: *"Kỳ báo cáo này chưa tới hạn. Vui lòng đợi đến thời hạn để lập báo cáo"*. Tham chiếu: CS_01.
- Mỗi TCKT chỉ thấy báo cáo của mình. Filter Dự án chỉ liệt kê dự án thuộc TCKT đang đăng nhập. Tham chiếu: **CMR_01**.
- Phân trang. Tham chiếu: CMR_10.

---

## UC227-231.2: Lập Báo Cáo

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Lập mới báo cáo tình hình thực hiện dự án đầu tư năm (Mẫu A.III.2)
- Báo cáo gồm 3 phần: **Phần A** (Form thông tin chung — 13 trường, trigger từ A-001), **Phần B** (eForm grid 2 cột dữ liệu — 13 mục chính với cấu trúc phân cấp, blocks NĐT lấy từ API), **Phần C** (Textarea khó khăn/vướng mắc).

Truy cập chức năng: Màn danh sách báo cáo (UC227-231.1) → Nhấn nút [Lập báo cáo]

Chức năng đáp ứng usecase số: 227, 228

---

### 2. Mô tả giao diện

#### PHẦN HEADER — KỲ BÁO CÁO

| # | Tên trường  | Kiểu trường | Giá trị mặc định                   | Được sửa | Bắt buộc | Mô tả/Ghi chú                                                                                            |
| - | -------------- | -------------- | --------------------------------------- | ------------ | ---------- | ----------------------------------------------------------------------------------------------------------- |
| 1 | Năm báo cáo | Read-only      | Theo kỳ báo cáo chọn từ Danh sách |              | x          | Auto-fill từ Kỳ hạn báo cáo tương ứng trên màn hình danh sách. Không cho phép sửa trên form |

---

#### PHẦN A: Thông tin chung về dự án đầu tư

| #  | Tên trường                       | Kiểu    | Giá trị mặc định | Được sửa | Bắt buộc | Ghi chú                                                                                                                                                                      |
| -- | ----------------------------------- | -------- | --------------------- | ------------ | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1  | Tên dự án / Tên Hợp đồng BCC | Dropdown | Null                  | x            | x          | Danh sách dự án từ API, chỉ hiển thị dự án thuộc TCKT đang đăng nhập. Khi chọn → hệ thống auto-fill. Tham chiếu:**CMR_01**, CMR_07, CMR_12, RULE-02. |
| 2  | Mã số dự án / Số GCNĐT        | Label    | Từ API               |              | x          | Read-only. Tham chiếu: CMR_12.                                                                                                                                               |
| 3  | Ngày cấp GCNĐKĐT                | Label    | Từ API               |              | x          | Read-only. dd/MM/yyyy. Tham chiếu: CMR_12.                                                                                                                                   |
| 4  | Cơ quan cấp GCNĐKĐT             | Label    | Từ API               |              | x          | Read-only. Tham chiếu: CMR_12.                                                                                                                                               |
| 5  | Địa điểm thực hiện dự án    | Label    | Từ API               |              | x          | Read-only. Tham chiếu: CMR_12.                                                                                                                                               |
| 6  | Tổng vốn đầu tư đăng ký     | Label    | Từ API               |              | x          | Read-only. Đơn vị: Triệu VNĐ (phân hệ ĐTTN). Tham chiếu: RULE-01, CMR_12.                                                          |
| 7  | Tên tổ chức kinh tế             | Label    | Từ API               |              | x          | Read-only. Tham chiếu: CMR_12.                                                                                                                                               |
| 8  | Mã số DN / MST                    | Label    | Từ API               |              | x          | Read-only. Tham chiếu: CMR_12.                                                                                                                                               |
| 9  | Ngày cấp lần đầu ĐKKD         | Label    | Từ API               |              | x          | Read-only. dd/MM/yyyy. Tham chiếu: CMR_12.                                                                                                                                   |
| 10 | Cơ quan cấp ĐKKD                 | Label    | Từ API               |              | x          | Read-only. Tham chiếu: CMR_12.                                                                                                                                               |
| 11 | Địa chỉ liên hệ                | Text     | Từ API               | x            | x          | Cho phép sửa (địa chỉ giao dịch có thể khác đăng ký). RULE-02: cảnh báo khi đổi dự án. Tham chiếu: CMR_06, CMR_12.                                         |
| 12 | Số điện thoại                   | Text     | Từ API               | x            | x          | Cho phép sửa. RULE-02. Tham chiếu: CMR_06, CMR_12.                                                                                                                         |
| 13 | Email                               | Text     | Từ API               | x            | x          | Cho phép sửa. Validate format email (phải chứa @ và domain). RULE-02. Tham chiếu: CMR_06, CMR_12.                                                                       |

---

#### PHẦN B: Tình hình thực hiện dự án đầu tư (eForm Grid)

> Cấu trúc eForm Grid — 2 cột dữ liệu: Tên chỉ tiêu | **(A) Số liệu thực hiện năm báo cáo** | **(B) Số liệu lũy kế từ khi được cấp GCNĐKĐT đến cuối năm báo cáo**

> **RULE-01:** Phân hệ ĐTTN: đơn vị mặc định là "Triệu VNĐ" (do dự án ĐTTN được cấp GCNĐKĐT bằng VNĐ). Riêng mục VI cố định "Triệu VNĐ", mục V dùng "Người", mục VII dùng đơn vị năng lượng riêng.

| STT | Tên chỉ tiêu | Loại cell | Được sửa | Bắt buộc | Cột (A) | Cột (B) | Đơn vị | Ghi chú |
|:----|:-------------|:----------|:---------|:---------|:--------|:--------|:-------|:--------|
| **I** | **Vốn đầu tư thực hiện** | Auto-calc | | x | Σ(A) mục 1,2,3 | Auto-calc | Triệu VNĐ | Tooltips: (I = 1+2+3) |
| 1 | Vốn góp | Auto-calc | | x | Σ(A) mục 1.1+1.2 | Auto-calc | Triệu VNĐ | Tooltips: (liệt kê theo từng NĐT) |
| 1.1 | Nhà đầu tư Việt Nam | Auto-calc | | x | Σ(A) tất cả block NĐT VN | Auto-calc | Triệu VNĐ | Xem bảng chi tiết Block NĐT bên dưới |
| 1.2 | Nhà đầu tư nước ngoài | Auto-calc | | x | Σ(A) tất cả block NĐT NN | Auto-calc | Triệu VNĐ | Xem bảng chi tiết Block NĐT bên dưới |
| 2 | Vốn vay | Auto-calc | | x | Σ(A) các dòng vay | Auto-calc | Triệu VNĐ | Tooltips: (2 = 2.a+2.b+2.c). Cho phép số âm |
| 2.a | Vay trong nước | Editable | x | x | Editable | Editable | Triệu VNĐ | Cho phép nhập số âm. Tham chiếu: CMR_05 |
| 2.b | Vay từ công ty mẹ ở nước ngoài | Editable | x | x | Editable | Editable | Triệu VNĐ | Cho phép nhập số âm. Tham chiếu: CMR_05 |
| 2.c | Vay nước ngoài khác | Editable | x | x | Editable | Editable | Triệu VNĐ | Cho phép nhập số âm. Tham chiếu: CMR_05 |
| 3 | Lợi nhuận tái đầu tư | Editable | x | x | Editable | Editable | Triệu VNĐ | Cho phép nhập số âm. Tham chiếu: CMR_05 |
| **II** | **Doanh thu thuần** | Editable | x | x | Editable | Locked | Triệu VNĐ | Tham chiếu: CMR_05 |
| **III** | **Giá trị hàng xuất khẩu** | Editable | x | x | Editable | Locked | Triệu VNĐ | Tham chiếu: CMR_05 |
| **IV** | **Giá trị hàng nhập khẩu** | Editable | x | x | Editable | Locked | Triệu VNĐ | Tham chiếu: CMR_05 |
| **V** | **Số lao động hiện có đến thời điểm báo cáo** | Auto-calc | | x | Σ(A) LĐ VN + LĐ NN | Locked | Người | Tooltips: (V = V.1+V.2). Cột (B) Locked — lũy kế không áp dụng cho chỉ tiêu thời điểm |
| V.1 | Lao động Việt Nam | Editable | x | x | Editable | Locked | Người | Tham chiếu: CMR_05 |
| V.2 | Lao động nước ngoài | Editable | x | x | Editable | Locked | Người | Tham chiếu: CMR_05 |
| **VI** | **Thu nhập bình quân tháng của người lao động** | Editable | x | x | Editable | Locked | Triệu VNĐ | Đơn vị cố định (không đổi theo RULE-01). Tham chiếu: CMR_05 |
| **VII** | **Tình hình sử dụng năng lượng** | Group header | | | Locked | Locked | — | |
| VII.1 | Điện | Editable | x | x | Editable | Locked | kWh | Tham chiếu: CMR_05 |
| VII.2 | Than | Editable | x | x | Editable | Locked | Tấn | Tham chiếu: CMR_05 |
| VII.3 | Dầu | Editable | x | x | Editable | Locked | Lít | Tham chiếu: CMR_05 |
| VII.4 | Khí LNG | Editable | x | x | Editable | Locked | m³ | Tham chiếu: CMR_05 |
| VII.5 | Các loại năng lượng khác (nếu có) | Editable | x | | Editable | Locked | Tự ghi | Textbox tự do cho tên ĐVT. Tham chiếu: CMR_05 |
| **VIII** | **Thuế và các khoản nộp ngân sách Nhà nước** | Editable | x | x | Editable | Locked | Triệu VNĐ | Tham chiếu: CMR_05 |
| **IX** | **Diện tích đất, mặt nước đã sử dụng (nếu có)** | Editable | x | | Editable | Locked | m² | Optional. Tham chiếu: CMR_05 |
| **X** | **Lợi nhuận sau thuế** | Editable | x | x | Editable | Locked | Triệu VNĐ | Tham chiếu: CMR_05 |
| **XI** | **Chi phí đầu tư, nghiên cứu và phát triển** | Editable | x | x | Editable | Editable | Triệu VNĐ | Tham chiếu: CMR_05 |
| **XII** | **Chi phí đầu tư xử lý và bảo vệ môi trường** | Editable | x | x | Editable | Editable | Triệu VNĐ | Tham chiếu: CMR_05 |
| **XIII** | **Nguồn gốc công nghệ sử dụng** | Text | x | | — | — | — | Full-width. Không thuộc cấu trúc 2 cột. Mô tả quốc gia xuất xứ máy móc. Tham chiếu: CMR_06 |

---

**Chi tiết cấu trúc Block NĐT (6 row/block — dữ liệu từ API):**

Áp dụng cho cả Block NĐT Việt Nam và Block NĐT nước ngoài, chỉ khác nhau ở row 2 (nhãn định danh). Dữ liệu NĐT chỉ lấy từ API theo dự án đã chọn, không cho phép thêm/xóa block thủ công.

| Row | Tên trường | Loại cell | Được sửa | Bắt buộc | Cột (A) | Cột (B) | Đơn vị | Ghi chú |
|:----|:-----------|:----------|:---------|:---------|:--------|:--------|:-------|:--------|
| 1 | Tên NĐT | API Label | | x | Σ(A) row 4+5+6 | Auto-calc | Triệu VNĐ | API IRC. Read-only. Tham chiếu: CMR_12. Dữ liệu chỉ lấy từ API, không cho phép sửa |
| 2 | Mã định danh | API Label | | x | Locked | Locked | — | API IRC. NĐT VN: "Mã số thuế: [giá trị]". NĐT NN: "MST/Số QĐ thành lập/Số hộ chiếu: [giá trị]". Read-only. Tham chiếu: CMR_12 |
| 3 | "Chia ra:" | Group header | | | Locked | Locked | — | Tiêu đề nhóm |
| 4 | Bằng tiền | Editable | x | x | Editable | Editable | Triệu VNĐ | Tham chiếu: CMR_05 |
| 5 | Máy móc, thiết bị | Editable | x | x | Editable | Editable | Triệu VNĐ | Tham chiếu: CMR_05 |
| 6 | Tài sản khác | Editable | x | x | Editable | Editable | Triệu VNĐ | Tham chiếu: CMR_05 |

Danh sách nhà đầu tư được lấy tự động từ API theo dự án đã chọn (A-001). Nếu dự án có nhiều NĐT, hệ thống hiển thị nhiều block tương ứng. Không cho phép thêm/xóa thủ công. Dữ liệu Tên NĐT và Mã định danh (row 1, 2) hoàn toàn từ API, read-only. Tham chiếu: **CMR_12**.

**Ghi chú mục 1.2 (NĐT nước ngoài):** Khi dự án không có NĐT nước ngoài: trên eForm ẩn toàn bộ block NĐT NN (mục 1.2). Khi Preview (CF_07.1), In (CF_05), Xuất (CF_04): hiển thị đầy đủ cấu trúc bảng mục 1.2 với giá trị trống.

---

#### PHẦN C: Khó khăn, vướng mắc

| # | Tên trường                                       | Kiểu    | Được sửa | Bắt buộc | Ghi chú                                                                                                                                                       |
| - | --------------------------------------------------- | -------- | ------------ | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1 | Cập nhật khó khăn, vướng mắc và kiến nghị | Textarea | x            |            | **Optional.** Placeholder: "Nhập Cập nhật khó khăn, vướng mắc và kiến nghị (Nêu cụ thể khó khăn, vướng mắc, kiến nghị và hướng giải quyết)". Hỗ trợ xuống dòng. Tham chiếu: CMR_06. |

---

#### GHI CHÚ
Vùng text tĩnh ở cuối form báo cáo, cung cấp các giải thích nghiệp vụ cho người dùng:
- Vốn vay = tổng vay trong kỳ trừ số trả nợ trong kỳ (bao gồm cả vay ngắn hạn, trung hạn và dài hạn)
- Đối với các dự án của nhà đầu tư trong nước, dự án được cấp Giấy chứng nhận đăng ký đầu tư hoặc quyết định chủ trương đầu tư bằng Việt Nam đồng thì đơn vị báo cáo là "Triệu VNĐ" (đã áp dụng mặc định cho phân hệ ĐTTN)
- Không báo cáo vào các ô đánh dấu "X"

---

#### CÁC BUTTON

| #  | Tên           | Mô tả                                                                                                                                         |
| -- | -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| B1 | Hủy           | Quay về Danh sách. Popup xác nhận nếu có dữ liệu chưa lưu. Tham chiếu: CF_01, CMR_18 (mục "Xử lý nút [Hủy]").                           |
| B2 | Xem            | Preview báo cáo (PDF). Tham chiếu: CF_07.1.                                                                                                  |
| B3 | Lưu nháp     | Lưu toàn bộ dữ liệu ở trạng thái Lưu nháp mà không cần validate đầy đủ. Tham chiếu: CF_01, CMR_18 (mục "Xử lý nút [Lưu nháp]"). |
| B4 | Nộp báo cáo | Validate toàn bộ trường bắt buộc và logic cross-field trước khi nộp. Tham chiếu: CF_01, CMR_18.                                              |

---

### 3. Mô tả các xử lý của chức năng

**Xử lý chung:** Tham chiếu CF_01.

- **Nguyên tắc trách nhiệm (API-sourced fields):** Dữ liệu auto-fill từ API chỉ mang tính chất gợi ý/tham khảo. Người dùng tạo báo cáo là người chịu trách nhiệm cuối cùng về nội dung đã nộp — hệ thống cho phép chỉnh sửa tất cả trường API-sourced trước khi Nộp.

**Xử lý đặc thù Mẫu A.III.2:**

**A. Thông tin chung về dự án đầu tư:**

- **Rule 01:** Khi người dùng chọn dự án, hệ thống gọi API và auto-fill toàn bộ thông tin ở mục A. Tham chiếu **CMR_12**: Nếu API lỗi -> Hiện Toast T05 và Enable các trường để nhập tay.
- **Rule 02:** Nếu người dùng đổi dự án (A-001) sau khi đã nhập liệu ở Phần B, hệ thống hiển thị popup cảnh báo P02: *"Thay đổi dự án sẽ xóa toàn bộ dữ liệu đã nhập ở Phần B. Bạn có muốn tiếp tục?"*. Nếu [Tiếp tục] -> Xóa trắng Phần B và ghi đè Phần A. Nếu [Hủy] -> Giữ nguyên dự án cũ.
- **Rule 03 (Validate Năm):** Năm báo cáo (#1) không được nhỏ hơn Năm cấp GCNĐKĐT (#4). Lỗi: *"Năm báo cáo không hợp lệ (Dự án bắt đầu từ năm {YYYY})"*

**B. Phần B — eForm Grid:**

- Tất cả Auto-calc cập nhật real-time khi có thay đổi.
- Đơn vị mặc định là "Triệu VNĐ" cho toàn bộ chỉ tiêu tài chính (phân hệ ĐTTN). Riêng mục VI cố định "Triệu VNĐ".
- **Validation Số:** Các trường I, II, III, IV, V, VI, VII, VIII, X, XI, XII chỉ cho phép số >= 0. Mục 2 (Vốn vay) và Mục 3 (Lợi nhuận tái đầu tư) cho phép số âm.

---

## UC227-231.3: Các Tác Vụ Bổ Trợ

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Các tác vụ bổ trợ – Xem chi tiết, Xem vòng đời, In, Xuất báo cáo, Nộp, Chỉnh sửa
- Cho phép người dùng thực hiện tác vụ tương ứng trạng thái bản ghi.

Truy cập chức năng: Màn danh sách báo cáo (UC227-231.1) → Cột Hành động

Chức năng đáp ứng usecase số: 229, 230, 231

---

### 2. Mô tả giao diện

| # | Tên            | Kiểu  | Điều kiện hiển thị                         | Mô tả                                          |
| - | --------------- | ------ | ----------------------------------------------- | ------------------------------------------------ |
| 1 | Nộp            | Button | Chỉ khi Lưu nháp hoặc Yêu cầu chỉnh sửa | Tham chiếu: CF_09.                              |
| 2 | Chỉnh sửa     | Button | Chỉ khi Lưu nháp hoặc Yêu cầu chỉnh sửa | Tham chiếu: CF_03.                              |
| 3 | Xem chi tiết   | Button | Tất cả trạng thái                           | Toàn bộ trường Disabled. Tham chiếu: CF_07. |
| 4 | Xem vòng đời | Button | Tất cả trạng thái                           | Popup Audit Trail. Tham chiếu: CF_06.           |
| 5 | In              | Button | Tất cả trạng thái                           | Tham chiếu: CF_05.                              |
| 6 | Xuất báo cáo          | Button | Tất cả trạng thái                           | Excel. **Chỉ từ Màn hình danh sách** (không có trong Preview). Nếu bản ghi có thay đổi chưa Lưu → hiển thị popup: *"Nội dung xuất file là bản đã lưu gần nhất. Vui lòng Lưu nháp trước khi xuất nếu muốn cập nhật."* Tham chiếu: CF_04.                       |
| 7 | Xóa            | Button | Lưu nháp**VÀ** chưa từng nộp        | Tham chiếu: CF_08.                              |

---

### 3. Mô tả các xử lý của chức năng

- Xem chi tiết: Tham chiếu: CF_07.
- Xem vòng đời: Tham chiếu: CF_06.
- In báo cáo: Tham chiếu: CF_05.
- Xuất báo cáo: Kết xuất ra file **Excel**. **Chỉ từ Màn hình danh sách** (không có trong Preview). Nếu bản ghi có thay đổi chưa Lưu → popup cảnh báo. Tham chiếu: CF_04.
- Chỉnh sửa: Tham chiếu: CF_03.

---

## 4. Lịch sử cập nhật

| Ngày      | Phiên bản | Mục cập nhật | Before | After | Ghi chú |
| ---------- | ----------- | -------------- | ------- | ------ | -------- |
| 2026-05-21 | 1.0         | Khởi tạo     | —      | —     | Tạo mới từ template UC047-052 (ĐTTN) |
| 2026-05-21 | 1.0 → 1.1 | appendices.md mục 2.4 DDI | UC227-232 = Quý/DDI_AI3, UC233-238 = Năm/DDI_AI2 | UC227-231 = Năm/DDI_AIII2, UC233-238 = Trước khi thực hiện/DDI_AIII3 | Q1 audit: BA xác nhận dải UC chính xác |
| 2026-05-21 | 1.0 → 1.1 | Phần B — Block NĐT NN empty state | (Không có) | "Khi không có NĐT NN: eForm ẩn block. Preview/In/Xuất hiển thị đầy đủ cấu trúc bảng với giá trị trống." | Q2 audit: Xác nhận behavior khi không có NĐT nước ngoài |
| 2026-05-21 | 1.1 → 1.2 | Phần B — Đơn vị eForm Grid + Block NĐT | "USD" | "Triệu VNĐ" | ĐTTN luôn dùng VNĐ → đơn vị mặc định là "Triệu VNĐ" |
| 2026-05-21 | 1.1 → 1.2 | RULE-01 | "Đổi label đơn vị từ USD sang Triệu VNĐ" | "Phân hệ ĐTTN: đơn vị mặc định là Triệu VNĐ" | Không còn conditional — ĐTTN luôn dùng Triệu VNĐ |
| 2026-05-22 | 1.2 → 1.3 | Mục 1, 2, 3 | Xóa nội dung phân quyền (Phân quyền: CMR_01/CMR_02/CMR_03) và cột Phân quyền trong bảng Action Mapping | — | Lược bỏ thông tin phân quyền theo yêu cầu |
