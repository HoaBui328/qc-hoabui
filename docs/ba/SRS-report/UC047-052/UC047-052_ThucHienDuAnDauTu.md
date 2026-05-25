# UC047-052: Báo cáo tình hình thực hiện dự án đầu tư năm ... (Mẫu A.III.2)

| Thuộc tính                            | Giá trị                                                               |
| --------------------------------------- | ----------------------------------------------------------------------- |
| **BA phụ trách**                | quan.trinh                                                              |
| **Phân hệ**                     | Quản lý đầu tư nước ngoài vào Việt Nam                        |
| **Mẫu biểu**                    | Mẫu A.III.2 2026.4.20 Phu luc A.III-IV                                 |
| **Loại báo cáo**               | Định kỳ năm (hạn nộp: trước 31/3 năm sau)                      |
| **Hình thức nộp**              | Báo cáo đơn lẻ theo từng dự án                                  |
| **Cơ quan nhận**                | Cơ quan đăng ký đầu tư + Cơ quan thống kê tại địa phương |
| **Đối tượng lập**            | Tổ chức kinh tế (TCKT) thực hiện dự án                           |
| **Giao diện**                    | User site                                                               |
| **Ngày tạo**                    | 2026-04-24                                                              |
| **Phiên bản**                   | 2.1                                                                     |
| **Quy tắc sinh mã báo cáo**   | FDI_AIII2_[ID]                                                          |
| **Loại quy trình**             | 2 bước (CMCĐT_BCTK_02, CMCĐT_BCTK_03)                                 |
| **Phạm vi dữ liệu đầu vào** | Có (chọn dự án)                                                     |

> **Lưu ý kiến trúc:** Báo cáo này do Tổ chức kinh tế thực hiện dự án lập. Mỗi báo cáo gắn với 1 dự án cụ thể. Cấu trúc gồm 3 phần: Phần A (Form thông tin chung), Phần B (eForm grid 2 cột dữ liệu), Phần C (Textarea tự do).

---

## UC047-052.1: Xem Danh Sách Báo Cáo

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Xem danh sách báo cáo tình hình thực hiện dự án đầu tư năm (Mẫu A.III.2)
- Chức năng cho phép Tổ chức kinh tế truy cập danh sách báo cáo định kỳ năm theo từng dự án, được nhóm theo Kỳ hạn báo cáo. Mỗi TCKT chỉ thấy báo cáo do mình lập.

Truy cập chức năng: Phân hệ Báo cáo → Quản lý ĐTNN vào VN → Báo cáo tình hình thực hiện dự án đầu tư năm (Mẫu A.III.2)

Chức năng đáp ứng usecase số: 47, 48, 49, 50, 51, 52

---

### 2. Mô tả giao diện

Giao diện: **Periodic-single** — Báo cáo có kỳ hạn năm, gửi lẻ từng dự án.

| #                                                     | Tên trường          | Kiểu trường              | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả                                                                                                                                                                                          |
| ----------------------------------------------------- | ---------------------- | --------------------------- | --------------------- | ------------ | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Khung Điều kiện Lọc & Tìm kiếm**        |                        |                             |                       |              |            |                                                                                                                                                                                                  |
| 1                                                     | Năm                   | Yearpicker                  | Năm hiện tại       | x            |            | Chọn năm; hệ thống lọc và nhóm danh sách theo năm. Kết quả hiển thị ngay. Tham chiếu: CMR_07.                                                                                      |
| 2                                                     | Trạng thái kỳ       | Multiple-selection Dropdown | Null                  | x            |            | Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo. Tham chiếu: CMR_04, CMR_07., CMR_16                                                                                                             |
| 3                                                     | Dự án                | Dropdown/Search             | Tất cả dự án | x            |            | Lọc theo dự án cụ thể. Danh sách chỉ hiển thị dự án thuộc TCKT đang đăng nhập. Tham chiếu:**CMR_01**. Tham chiếu: CMR_16.  Tham chiếu: CMR_16. |
| 4                                                     | Trạng thái báo cáo | Multiple-selection Dropdown | Null                  | x            |            | Người dùng chọn một hoặc nhiều giá trị: Lưu nháp / Chờ duyệt / Đã tiếp nhận / Yêu cầu chỉnh sửa. Kết quả lọc hiển thị ngay sau khi chọn. Tham chiếu: CMR_03, CMR_07., CMR_16 |
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
| 14                                                    | Hành động           | Button group                | Null                  |              |            | Chi tiết tham chiếu: UC047-052.3.                                                                                                                                                              |

---

### 3. Mô tả các xử lý của chức năng

- Hệ thống nhóm danh sách theo Kỳ hạn (năm), mặc định collapse. Sắp xếp giảm dần.
- Nút [Lập báo cáo] và [Nhập từ file] Chỉ hiển thị khi Trong thời hạn. Ẩn khi Chưa tới hạn hoặc Qua kỳ báo cáo. Tham chiếu: CF_01, CMR_18.
- Khi kỳ hạn ở trạng thái Chưa tới hạn, hiển thị Empty state: *"Kỳ báo cáo này chưa tới hạn. Vui lòng đợi đến thời hạn để lập báo cáo"*. Tham chiếu: CS_01.
- Mỗi TCKT chỉ thấy báo cáo của mình. Filter Dự án chỉ liệt kê dự án thuộc TCKT đang đăng nhập. Tham chiếu: **CMR_01**.
- Phân trang. Tham chiếu: CMR_10.

---

## UC047-052.2: Lập Báo Cáo

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Lập mới báo cáo tình hình thực hiện dự án đầu tư năm (Mẫu A.III.2)
- Báo cáo gồm 3 phần: **Phần A** (Form thông tin chung — 13 trường, trigger từ A-001), **Phần B** (eForm grid 2 cột dữ liệu — 13 mục chính với cấu trúc phân cấp, blocks NĐT lấy từ API), **Phần C** (Textarea khó khăn/vướng mắc).

Truy cập chức năng: Màn danh sách báo cáo (UC047-052.1) → Nhấn nút [Lập báo cáo]

Chức năng đáp ứng usecase số: 47, 48

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
| 6  | Tổng vốn đầu tư đăng ký     | Label    | Từ API               |              | x          | Read-only. Đơn vị tiền tệ (USD hoặc Triệu VNĐ) linh động theo loại dự án. Tham chiếu: RULE-01, CMR_12.                                                          |
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

> **RULE-01:** Đối với dự án NĐT trong nước cấp GCNĐKĐT bằng VNĐ, toàn bộ label đơn vị từ "USD" đổi sang "Triệu VNĐ". Riêng mục VI cố định "triệu VNĐ".

| STT | Tên chỉ tiêu | Loại cell | Được sửa | Bắt buộc | Cột (A) | Cột (B) | Đơn vị | Ghi chú |
|:----|:-------------|:----------|:---------|:---------|:--------|:--------|:-------|:--------|
| **I** | **Vốn đầu tư thực hiện** | Auto-calc | | x | Σ(A) mục 1,2,3 | Auto-calc | USD | Tooltips: (I = 1+2+3) |
| 1 | Vốn góp | Auto-calc | | x | Σ(A) mục 1.1+1.2 | Auto-calc | USD | Tooltips: (liệt kê theo từng NĐT) |
| 1.1 | Nhà đầu tư Việt Nam | Auto-calc | | x | Σ(A) tất cả block NĐT VN | Auto-calc | USD | Xem bảng chi tiết Block NĐT bên dưới |
| 1.2 | Nhà đầu tư nước ngoài | Auto-calc | | x | Σ(A) tất cả block NĐT NN | Auto-calc | USD | Xem bảng chi tiết Block NĐT bên dưới |
| 2 | Vốn vay | Auto-calc | | x | Σ(A) các dòng vay | Auto-calc | USD | Tooltips: (2 = 2.a+2.b+2.c). Cho phép số âm |
| 2.a | Vay trong nước | Editable | x | x | Editable | Editable | USD | Cho phép nhập số âm. Tham chiếu: CMR_05 |
| 2.b | Vay từ công ty mẹ ở nước ngoài | Editable | x | x | Editable | Editable | USD | Cho phép nhập số âm. Tham chiếu: CMR_05 |
| 2.c | Vay nước ngoài khác | Editable | x | x | Editable | Editable | USD | Cho phép nhập số âm. Tham chiếu: CMR_05 |
| 3 | Lợi nhuận tái đầu tư | Editable | x | x | Editable | Editable | USD | Cho phép nhập số âm. Tham chiếu: CMR_05 |
| **II** | **Doanh thu thuần** | Editable | x | x | Editable | Locked | USD | Tham chiếu: CMR_05 |
| **III** | **Giá trị hàng xuất khẩu** | Editable | x | x | Editable | Locked | USD | Tham chiếu: CMR_05 |
| **IV** | **Giá trị hàng nhập khẩu** | Editable | x | x | Editable | Locked | USD | Tham chiếu: CMR_05 |
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
| **VIII** | **Thuế và các khoản nộp ngân sách Nhà nước** | Editable | x | x | Editable | Locked | USD | Tham chiếu: CMR_05 |
| **IX** | **Diện tích đất, mặt nước đã sử dụng (nếu có)** | Editable | x | | Editable | Locked | m² | Optional. Tham chiếu: CMR_05 |
| **X** | **Lợi nhuận sau thuế** | Editable | x | x | Editable | Locked | USD | Tham chiếu: CMR_05 |
| **XI** | **Chi phí đầu tư, nghiên cứu và phát triển** | Editable | x | x | Editable | Editable | USD | Tham chiếu: CMR_05 |
| **XII** | **Chi phí đầu tư xử lý và bảo vệ môi trường** | Editable | x | x | Editable | Editable | USD | Tham chiếu: CMR_05 |
| **XIII** | **Nguồn gốc công nghệ sử dụng** | Text | x | | — | — | — | Full-width. Không thuộc cấu trúc 2 cột. Mô tả quốc gia xuất xứ máy móc. Tham chiếu: CMR_06 |

---

**Chi tiết cấu trúc Block NĐT (6 row/block — dữ liệu từ API):**

Áp dụng cho cả Block NĐT Việt Nam và Block NĐT nước ngoài, chỉ khác nhau ở row 2 (nhãn định danh). Dữ liệu NĐT chỉ lấy từ API theo dự án đã chọn, không cho phép thêm/xóa block thủ công.

| Row | Tên trường | Loại cell | Được sửa | Bắt buộc | Cột (A) | Cột (B) | Đơn vị | Ghi chú |
|:----|:-----------|:----------|:---------|:---------|:--------|:--------|:-------|:--------|
| 1 | Tên NĐT | API Label | | x | Σ(A) row 4+5+6 | Auto-calc | USD | API IRC. Read-only. Tham chiếu: CMR_12. Dữ liệu chỉ lấy từ API, không cho phép sửa |
| 2 | Mã định danh | API Label | | x | Locked | Locked | — | API IRC. NĐT VN: "Mã số thuế: [giá trị]". NĐT NN: "MST/Số QĐ thành lập/Số hộ chiếu: [giá trị]". Read-only. Tham chiếu: CMR_12 |
| 3 | "Chia ra:" | Group header | | | Locked | Locked | — | Tiêu đề nhóm |
| 4 | Bằng tiền | Editable | x | x | Editable | Editable | USD | Tham chiếu: CMR_05 |
| 5 | Máy móc, thiết bị | Editable | x | x | Editable | Editable | USD | Tham chiếu: CMR_05 |
| 6 | Tài sản khác | Editable | x | x | Editable | Editable | USD | Tham chiếu: CMR_05 |

Danh sách nhà đầu tư được lấy tự động từ API theo dự án đã chọn (A-001). Nếu dự án có nhiều NĐT, hệ thống hiển thị nhiều block tương ứng. Không cho phép thêm/xóa thủ công. Dữ liệu Tên NĐT và Mã định danh (row 1, 2) hoàn toàn từ API, read-only. Tham chiếu: **CMR_12**.

---

#### PHẦN C: Khó khăn, vướng mắc

| # | Tên trường                                       | Kiểu    | Được sửa | Bắt buộc | Ghi chú                                                                                                                                                       |
| - | --------------------------------------------------- | -------- | ------------ | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1 | Cập nhật khó khăn, vướng mắc và kiến nghị | Textarea | x            |            | **Optional.** Placeholder: "Nhập Cập nhật khó khăn, vướng mắc và kiến nghị (Nêu cụ thể khó khăn, vướng mắc, kiến nghị và hướng giải quyết)". Hỗ trợ xuống dòng. Tham chiếu: CMR_06. |

---

#### GHI CHÚ
Vùng text tĩnh ở cuối form báo cáo, cung cấp các giải thích nghiệp vụ cho người dùng:
- Vốn vay = tổng vay trong kỳ trừ số trả nợ trong kỳ (bao gồm cả vay ngắn hạn, trung hạn và dài hạn)
- Đối với các dự án của nhà đầu tư trong nước, dự án được cấp Giấy chứng nhận đăng ký đầu tư hoặc quyết định chủ trương đầu tư bằng Việt Nam đồng thì đơn vị báo cáo là "Triệu VNĐ"
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
- Khi dự án lấy về có phân loại VNĐ → hệ thống đổi toàn bộ label đơn vị từ "USD" sang "Triệu VNĐ" ở Phần A ("Tổng vốn đầu tư đăng ký") và Phần B. Riêng mục VI cố định "triệu VNĐ".
- **Validation Số:** Các trường I, II, III, IV, V, VI, VII, VIII, X, XI, XII chỉ cho phép số >= 0. Mục 2 (Vốn vay) và Mục 3 (Lợi nhuận tái đầu tư) cho phép số âm.

---

## UC047-052.3: Các Tác Vụ Bổ Trợ

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Các tác vụ bổ trợ – Xem chi tiết, Xem vòng đời, In, Xuất báo cáo, Nộp, Chỉnh sửa
- Cho phép người dùng thực hiện tác vụ tương ứng trạng thái bản ghi.

Truy cập chức năng: Màn danh sách báo cáo (UC047-052.1) → Cột Hành động

Chức năng đáp ứng usecase số: 49, 50, 51, 52

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

| Ngày      | Phiên bản | Mục cập nhật                                      | Before                                                                                                               | After                                                                                                                                                                                                        | Ghi chú                                                       |
| ---------- | ----------- | ---------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------- |
| 2026-05-03 | N/A         | Trạng thái báo cáo                               | Đã nộp                                                                                                            | Chờ duyệt / Đã tiếp nhận                                                                                                                                                                               | Thay đổi theo bộ trạng thái mới của hệ thống (CMR_03) |
| 2026-05-05 | 1.0 → 1.1  | Phần A, trường #3–#14 (API-sourced)              | Không tham chiếu CMR_12, chưa quy định hành vi khi API null                                                    | Bổ sung tham chiếu CMR_12 cho toàn bộ 12 trường lấy từ API. Khi API null → Enabled cho nhập thủ công, validate theo kiểu dữ liệu, placeholder "Nhập thủ công", ghi nhận source manual/api | Đồng bộ với CMR_12 v1.4                                    |
| 2026-05-05 | 1.1 → 1.2  | Phần B (eForm Grid)                                 | Bảng grid tách riêng với cột (A)/(B) chứa ký hiệu ED/AC/LK, kèm bảng "Quy ước 5 loại cell" riêng biệt | Chuyển sang format eForm row trong cùng bảng giao diện. Hành vi từng cột mô tả trong Ghi chú. Xóa bảng "Quy ước 5 loại cell" và dòng ký hiệu                                              | Thống nhất format mô tả eForm Grid với UC059-064          |
| 2026-05-05 | 1.2 → 1.3  | Phần A #2 Tên dự án (Dropdown)                   | Tham chiếu: CMR_02, RULE-02                                                                                         | Tham chiếu: CMR_02, CMR_07, CMR_12, RULE-02                                                                                                                                                                 | Bổ sung CMR_07, CMR_12 cho Dropdown lấy dữ liệu từ API    |
| 2026-05-05 | 1.2 → 1.3  | Phần A #12 Địa chỉ, #13 SĐT, #14 Email          | Tham chiếu: CMR_12                                                                                                  | Tham chiếu: CMR_06, CMR_12                                                                                                                                                                                  | Bổ sung CMR_06 cho trường Text editable                     |
| 2026-05-05 | 1.2 → 1.3  | Phần B mục 2 Vốn vay (tooltip)                    | Không có tham chiếu CMR                                                                                           | Tham chiếu: CMR_11                                                                                                                                                                                          | Bổ sung CMR_11 cho trường có tooltip                       |
| 2026-05-05 | 1.2 → 1.3  | Phần C #1 Khó khăn vướng mắc (Textarea)        | Không có tham chiếu CMR                                                                                           | Tham chiếu: CMR_06                                                                                                                                                                                          | Bổ sung CMR_06 cho Textarea                                   |
| 2026-05-08 | 1.3 → 1.4  | Audit chuyên sâu & UX update                       | v1.3 - Sai actor, thiếu nút, rule xóa block mặc định                                                           | Đổi sang CMR_01, thêm nút [Xem chi tiết], gán mã V17, popup xóa block có data, cảnh báo đổi dự án và validate số âm/dương                                                                | Thực hiện theo kế hoạch audit chuyên sâu                 |
| 2026-05-12 | 1.4 → 1.5  | Phần A — #1 Năm báo cáo — Validate min year    | Danh sách năm ≤ hiện tại                                                                                        | Danh sách năm**từ 1987** đến hiện tại. Validate min: ≥ 1987. Lỗi inline: *"Năm báo cáo không được nhỏ hơn 1987."*                                                                  | Chuẩn hóa mốc năm 1987 theo quy định hệ thống          |
| 2026-05-11 | 1.0→1.1    | Quy tắc sinh mã báo cáo                          | `DTNN_A3_2_[ID]`                                                                                                   | `FDI_AIII2_[ID]`                                                                                                                                                                                           | Chuẩn hóa prefix và mã theo appendices.md v2.0 (INS-10)    |
| 2026-05-11 | +1          | Kiểu field Năm báo cáo                           | `Number`                                                                                                           | `Yearpicker`                                                                                                                                                                                               | Đồng nhất kiểu field (INS-04)                              |
| 2026-05-11 | +1          | Dòng phân cách bảng Markdown                     | Thiếu cột (3 chỗ)                                                                                                 | Đủ số cột theo header                                                                                                                                                                                    | Chuẩn hóa separator (INS-05)                                 |
| 2026-05-11 | +1          | Dòng phân cách Markdown                           | Sai số cột                                                                                                         | 3 cột đúng                                                                                                                                                                                                | Sửa lỗi Markdown (INS-05)                                    |
| 2026-05-14 | 1.5 → 1.6  | UC047-052.2 Mục 3 — Decimal precision              | (Không có)                                                                                                         | Bổ sung: Phần thập phân tối đa 5 chữ số, auto-round half-up khi blur                                                                                                                                 | Chuẩn hóa precision toàn hệ thống                         |
| 2026-05-14 | 1.5 → 1.6  | UC047-052.2 Mục 3 — Nguyên tắc trách nhiệm API | (Không có)                                                                                                         | Bổ sung: User tạo báo cáo chịu trách nhiệm cuối cùng, API-sourced fields Enabled cho sửa                                                                                                           | User chịu trách nhiệm cuối về dữ liệu đã nộp         |
| 2026-05-14 | 1.5 → 1.6  | UC047-052.2 Mục 3 — Max length mặc định         | (Không có)                                                                                                         | Bổ sung: Textbox 500, Textarea 2000, Number 20, Search 200 ký tự                                                                                                                                          | Chuẩn hóa validation rules toàn hệ thống                  |
| 2026-05-15 | 1.6 → 1.7  | Header — Năm báo cáo | Yearpicker Editable trong Phần A (#1) | Chuyển sang PHẦN HEADER, Read-only, auto-fill từ kỳ hạn trên danh sách. Không cho sửa trên form | Đồng bộ với UC041-046 v1.5 |
| 2026-05-15 | 1.6 → 1.7  | Phần B — Restructure format bảng | Bảng đơn cột Ghi chú chứa mô tả Cột (A)/(B) | Tách thành bảng có cột riêng: STT / Tên chỉ tiêu / Loại cell / Được sửa / Bắt buộc / Cột (A) / Cột (B) / Đơn vị / Ghi chú | Đồng bộ format với UC041-046 |
| 2026-05-15 | 1.6 → 1.7  | Phần B — Mục V label | "Số lao động (= V.1+V.2)" | "Số lao động hiện có đến thời điểm báo cáo (= V.1+V.2)" + ghi chú: lũy kế không áp dụng cho chỉ tiêu thời điểm | Cập nhật theo biểu mẫu gốc |
| 2026-05-15 | 1.6 → 1.7  | Phần B — Block NĐT format | Bảng 6 cột (Row/Tên/Kiểu/Sửa/BB/Ghi chú) | Tách thành bảng có cột Cột (A) / Cột (B) / Đơn vị riêng biệt | Đồng bộ format |
| 2026-05-15 | 1.7 → 1.8  | Loại bỏ Thêm/Xóa NĐT | Cấu trúc lặp động, có nút [+ Thêm NĐT VN/NN], [Xóa NĐT], popup P04, tham chiếu CMR_15 | Danh sách NĐT lấy tự động từ API, hiển thị nhiều block nếu có nhiều NĐT, không cho thêm/xóa thủ công. Dữ liệu Tên + Mã định danh hoàn toàn từ API | Đồng bộ với UC041-046 v1.3. NĐT chỉ lấy qua API |
| 2026-05-15 | 1.7 → 1.8  | Xóa Rule 04 (MST) | Rule 04: Khi nhập tay NĐT, kiểm tra trùng MST. Lỗi inline | (Đã xóa) — không còn nhập tay NĐT nên Rule 04 không áp dụng | Hệ quả của việc loại bỏ Thêm NĐT thủ công |
| 2026-05-15 | 1.8 → 1.9  | Phần B — XIII kiểu field | Textarea | Text (Input 1 dòng) | Đồng bộ với UI mockup |
| 2026-05-15 | 1.8 → 1.9  | Phần B — Mục 2 Vốn vay tooltip | Tooltip icon (?): giải thích công thức. Tham chiếu CMR_11 | Xóa tooltip — nội dung đã nằm trong vùng GHI CHÚ cuối form | Đồng bộ với UI mockup |
| 2026-05-15 | 1.8 → 1.9  | Phần B — VII.5 Thêm năng lượng | Nút [+ Thêm loại năng lượng] | (Đã xóa) — chỉ 1 dòng VII.5 cố định | Đồng bộ với UI mockup |
| 2026-05-15 | 1.9 → 2.0  | Phần B — Mục I label | Vốn đầu tư thực hiện **(= 1+2+3)** | Vốn đầu tư thực hiện — công thức chuyển sang Tooltips | Đồng bộ với UI mockup |
| 2026-05-15 | 1.9 → 2.0  | Phần B — Mục 2 label | Vốn vay **(= Σ 3 dòng con)** | Vốn vay — công thức chuyển sang Tooltips: (2 = 2.a+2.b+2.c) | Đồng bộ với UI mockup |
| 2026-05-15 | 1.9 → 2.0  | Phần B — Mục V label | Số lao động hiện có đến thời điểm báo cáo **(= V.1+V.2)** | Số lao động hiện có đến thời điểm báo cáo — công thức chuyển sang Tooltips: (V = V.1+V.2) | Đồng bộ với UI mockup |
| 2026-05-17 | CMR v2.0 | Them tham chieu CMR_16 (2 dong filter dropdown) | Chua co CMR_16 | Them , CMR_16 sau CMR_07 tren cac dong Multiple-selection Dropdown | Filter dropdown phai co option Tat ca (CMR_16) |
| 2026-05-17 | CMR v2.0 | Them tham chieu CMR_18 (Tab Navigation) | Chua co CMR_18 | Them CMR_18 vao tham chieu CF_01 | Tuan thu CMR_18 Tab Navigation tren form nhap lieu |
| 2026-05-17 | CMR v2.0 | STD-04b Search placeholder fix (1) | Tim kiem theo... | Tim kiem nhanh theo ma bao cao | Chuan hoa CMR_06 STD-04b |
| 2026-05-17 | CMR v2.0 | STD-01 Filter | Chua co CMR_16/Tat ca | Them Tat ca du an va CMR_16 | Dong bo |
| 2026-05-17 | CMR v2.0 | STD-04a Custom Placeholder | 1 truong khong chuan | Dong bo Nhap [ten truong] (Goi y) | CMR_06 |
| 2026-05-18 | CMR v2.0 -> 2.1 | Thuật ngữ nút bấm | Export / Import | Xuất báo cáo / Nhập từ file | Cập nhật đồng bộ tiếng Việt |
| 2026-05-19 | 2.0 → 2.1 | UC047-052.1 Mục 3 — Xóa Column Sort | Bổ sung: Cột Ngày/Số hiển thị icon Sort trên header. Single-column sort. Client-side | (Đã xóa) — thông tin sai, không có yêu cầu từ BA | Xóa đặc tả Column Sort khỏi SRS |
| 2026-05-19 | 2.0 → 2.1 | UC047-052.2 Mục 3 — Xóa Decimal precision + Max length | Decimal precision auto-round 5 chữ số + Max length Textbox 500/Textarea 2000/Number 20/Search 200 | (Đã xóa) — tuân thủ CMR_05 v2.0 "Không cắt thập phân" + Numeric max 18, Text max 500 | Xóa rule ghi đè CMR_05/CMR_06 |
| 2026-05-22 | 2.0 → 2.1 | Phân quyền (Lưu ý kiến trúc, UC047-052.1, .2, .3) + Action Mapping cột Phân quyền | Nội dung phân quyền inline + cột Phân quyền trong bảng Action Mapping | (Đã xóa) | Lược bỏ nội dung phân quyền theo yêu cầu tách riêng |
