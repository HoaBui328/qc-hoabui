# UC221-226: Báo cáo tình hình thực hiện dự án đầu tư quý … năm … (Mẫu A.III.1)

| Thuộc tính                            | Giá trị                                                              |
| --------------------------------------- | ---------------------------------------------------------------------- |
| **BA phụ trách**                | quan.trinh                                                             |
| **Phân hệ**                     | Quản lý đầu tư trong nước Việt Nam                             |
| **Mẫu biểu**                    | Mẫu A.III.1                                                           |
| **Loại báo cáo**               | Định kỳ quý                                                        |
| **Hình thức nộp**              | Báo cáo đơn lẻ (Single report form)                               |
| **Phạm vi dữ liệu đầu vào** | Có — chọn Dự án                                                   |
| **Hạn nộp**                     | Trước ngày 10 tháng đầu của quý sau quý báo cáo             |
| **File xuất**                    | Excel                                                                  |
| **Cơ quan nhận**                | Cơ quan đăng ký đầu tư; Cơ quan thống kê tại địa phương |
| **Đối tượng lập**            | Tổ chức kinh tế thực hiện dự án                                 |
| **Giao diện**                    | User site                                                              |
| **Ngày tạo**                    | 2026-05-21                                                             |
| **Phiên bản**                   | 1.3                                                                    |
| **Quy tắc sinh mã báo cáo**   | DDI_AIII1_[ID]                                                         |
| **Loại quy trình**              | 2 bước (CMCĐT_BCTK_02, CMCĐT_BCTK_03)                              |

---

## UC221-226.1: Xem Danh Sách Báo Cáo

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Xem danh sách Báo cáo tình hình thực hiện dự án đầu tư quý (Mẫu A.III.1)
- Chức năng cho phép Tổ chức kinh tế (TCKT) và Nhà đầu tư (NĐT) thành viên truy cập màn hình chính để theo dõi danh sách các báo cáo định kỳ quý về tình hình thực hiện dự án đầu tư. Áp dụng luồng nghiệp vụ Case A (ĐTNN/ĐTTN). Tham chiếu: CMR_01.

Truy cập chức năng: Phân hệ Báo cáo → Quản lý đầu tư trong nước Việt Nam → Báo cáo tình hình thực hiện dự án đầu tư quý

Chức năng đáp ứng usecase số: 221, 222, 223, 224, 225, 226

Mapping chi tiết:

| UC    | Chức năng                                   |
| ----- | --------------------------------------------- |
| UC221 | Lập + Lưu nháp + Nộp báo cáo            |
| UC222 | Xem + Lọc + Xuất báo cáo + Nhập từ file |
| UC223 | Chỉnh sửa báo cáo                         |
| UC224 | Phê duyệt (nộp) báo cáo                  |
| UC225 | Xem lịch sử + Xem vòng đời               |
| UC226 | In báo cáo                                  |

---

### 2. Mô tả giao diện

**Giao diện danh sách**

Giao diện: **Periodic-single** — Giao diện mẫu cho báo cáo có kỳ hạn (theo quý) và gửi lẻ từng báo cáo.

Mô tả giao diện:

| #                                                     | Tên trường          | Kiểu trường              | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả                                                                                                                                                                                                                                                   |
| ----------------------------------------------------- | ---------------------- | --------------------------- | --------------------- | ------------ | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Khung Điều kiện Lọc & Tìm kiếm**        |                        |                             |                       |              |            |                                                                                                                                                                                                                                                           |
| 1                                                     | Thanh tìm kiếm       | Search bar                  | Null                  | x            |            | Tìm theo**Mã báo cáo**, **Tên dự án**. Kết quả hiển thị ngay khi nhập. Nếu không tìm thấy: hiển thị "Không tìm thấy kết quả". Tham chiếu: CMR_06, CMR_09. Placeholder: "Tìm kiếm nhanh theo mã báo cáo, tên dự án". |
| 2                                                     | Dự án                | Dropdown + Searchable       | Tất cả dự án | x            |            | Lọc danh sách theo dự án mà TCKT/NĐT có liên quan. Tham chiếu: CMR_07. Tham chiếu: CMR_16. |
| 3                                                     | Năm                   | Yearpicker                  | Năm hiện tại       | x            |            | Người dùng nhấp để chọn năm từ calendar picker. Hệ thống lọc và nhóm danh sách theo năm được chọn. Kết quả hiển thị ngay lập tức, không cần nhấn thêm nút. Tham chiếu: CMR_07.                                            |
| 4                                                     | Trạng thái kỳ hạn  | Multiple-selection Dropdown | Null                  | x            |            | Người dùng chọn một hoặc nhiều giá trị: Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo. Kết quả lọc hiển thị ngay sau khi chọn. Tham chiếu: CMR_04, CMR_07, CMR_16.                                                                       |
| 5                                                     | Trạng thái báo cáo | Multiple-selection Dropdown | Null                  | x            |            | Người dùng chọn một hoặc nhiều giá trị: Lưu nháp / Chờ duyệt / Đã tiếp nhận / Yêu cầu chỉnh sửa. Kết quả lọc hiển thị ngay sau khi chọn. Tham chiếu: CMR_03, CMR_07, CMR_16.                                                          |
| **Khung Danh sách Kỳ hạn**                   |                        |                             |                       |              |            |                                                                                                                                                                                                                                                           |
| 6                                                     | Kỳ hạn báo cáo     | Label                       | Null                  |              |            | Hiển thị tên kỳ hạn (VD: "Quý 1/2026"). Mặc định collapse; người dùng click để expand danh sách báo cáo bên trong. Tham chiếu: CMR_08.                                                                                                 |
| 7                                                     | Trạng thái kỳ       | Label                       | Null                  |              |            | Hiển thị trạng thái của kỳ hạn: Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo. Tham chiếu: CMR_04.                                                                                                                                       |
| 8                                                     | Lập báo cáo         | Button                      | Null                  |              |            | Hiển thị trong header của mỗi kỳ. Chỉ hiển thị khi Trong thời hạn. Ẩn khi Chưa tới hạn hoặc đã Qua kỳ báo cáo. Tham chiếu: CF_01.                                                                                                    |
| 9                                                     | Nhập từ file                 | Button                      | Null                  |              |            | Hiển thị trong header của mỗi kỳ. Chỉ hiển thị khi Trong thời hạn. Ẩn khi Chưa tới hạn hoặc đã Qua kỳ báo cáo. Tham chiếu: CF_02 Case 1 (có Phạm vi dữ liệu nguồn input = Dự án).                                             |
| **Khung Danh sách Báo cáo** (trong mỗi kỳ) |                        |                             |                       |              |            |                                                                                                                                                                                                                                                           |
| 10                                                    | Tên dự án           | Label                       | Null                  |              |            | Hiển thị tên đầy đủ của dự án đầu tư.                                                                                                                                                                                                        |
| 11                                                    | Mã báo cáo          | Label                       | Null                  |              |            | Hiển thị mã báo cáo do hệ thống sinh theo quy tắc. Tham chiếu: CMR_09.                                                                                                                                                                           |
| 12                                                    | Kỳ báo cáo          | Label                       | Null                  |              |            | Hiển thị: Quý [Q] / Năm [YYYY].                                                                                                                                                                                                                       |
| 13                                                    | Ngày cập nhật       | Label                       | Null                  |              |            | Thời điểm thao tác gần nhất. Định dạng: dd/MM/yyyy HH:mm.                                                                                                                                                                                        |
| 14                                                    | Trạng thái           | Label                       | Null                  |              |            | Tham chiếu: CMR_03. Tại màn hình danh sách của NĐT thành viên, bản ghi hiển thị Tooltip:*"Đã được lập bởi [Tên TCKT đã lập báo cáo]"*. Tham chiếu: CMR_01, CS_01.                                                             |
| 15                                                    | Hành động           | Button group                | Null                  |              |            | Hiển thị các nút thao tác theo trạng thái bản ghi và phân quyền. Chi tiết tham chiếu: UC221-226.3.                                                                                                                                           |

---

### 3. Mô tả các xử lý của chức năng

- Hệ thống tự động nhóm danh sách theo Kỳ hạn báo cáo (theo quý/năm), mặc định collapse. Người dùng click để expand từng kỳ.
- Sắp xếp kỳ hạn giảm dần (kỳ mới nhất lên đầu). Báo cáo trong mỗi kỳ sắp xếp mới → cũ.
- Các nút [Lập báo cáo] và [Nhập từ file] bị ẩn với kỳ chưa bắt đầu (Chưa tới hạn) và kỳ đã qua (Qua kỳ báo cáo). Tham chiếu: CF_01.
- Bản ghi đã tồn tại (Lưu nháp / Yêu cầu chỉnh sửa) vẫn có thể Chỉnh sửa, Nộp, Xóa khi kỳ đã "Qua kỳ báo cáo" — CMR_04 chỉ ẩn nút [Lập báo cáo]/[Nhập từ file], không ảnh hưởng hành động trên bản ghi hiện hữu (theo CMR_03).
- Tất cả bộ lọc hiển thị kết quả ngay lập tức sau khi tương tác, không cần nhấn thêm nút.
- Phân trang. Tham chiếu: CMR_10.
- TCKT chỉ thấy báo cáo do chính họ tạo ra. NĐT thành viên thấy được báo cáo thuộc dự án mình tham gia. Tham chiếu: CMR_01, CS_01.
- Empty state — chưa có kỳ hạn nào: hiển thị "Chưa có báo cáo nào."

---

## UC221-226.2: Lập Báo Cáo

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Lập mới Báo cáo tình hình thực hiện dự án đầu tư quý (Mẫu A.III.1)
- Chức năng cho phép TCKT nhập liệu và khởi tạo báo cáo định kỳ quý. Hệ thống lấy thông tin cơ bản của dự án và TCKT từ API để tự động điền một số trường. Toàn bộ các trường khác đều cho phép nhập liệu tự do.

Điều kiện tiên quyết (Preconditions):

| # | Điều kiện | Ghi chú |
|---|---|---|
| PRE-01 | Người dùng đã đăng nhập với vai trò TCKT hoặc NĐT thành viên | CMR_01 |
| PRE-02 | Dự án thuộc TCKT đang đăng nhập đã tồn tại trên hệ thống | CMR_01 |
| PRE-03 | Kỳ hạn báo cáo ở trạng thái "Trong thời hạn" (để tạo mới) | CMR_04 |
| PRE-04 | API IRC/GCNĐKĐT và API ĐKKD khả dụng (cho auto-fill; fallback: nhập tay khi API lỗi) | CMR_12 |

Truy cập chức năng: Màn danh sách báo cáo (UC221-226.1) → Nhấn nút [Lập báo cáo]

Chức năng đáp ứng usecase số: 221, 222

---

### 2. Mô tả giao diện

**Quy ước chung áp dụng cho toàn bộ Biểu mẫu:**

Báo cáo được thiết kế bao gồm các phần:

Form thông tin chung (Phần A), eForm bảng/grid nhập liệu chi tiết (Phần B) và trường nhập liệu tự do (Phần C).

Đối với eForm grid ở Phần B, mỗi chỉ tiêu là một row trong grid. Mỗi row có cột "Tên chỉ tiêu" hiển thị tên chỉ tiêu, và ba cột dữ liệu: cột (A) là "Số liệu thực hiện trong quý báo cáo", cột (B) là "Số liệu lũy kế từ đầu năm đến cuối quý báo cáo", cột (C) là "Số liệu lũy kế từ khi được cấp GCNĐKĐT đến cuối quý báo cáo".

Tồn tại năm loại cell chính:

(1) Editable — ô người dùng nhập số liệu thực tế, nền trắng;

(2) Auto-calc — ô hệ thống tự tính tổng từ các dòng con, nền xám nhạt, không cho chỉnh sửa;

(3) Locked (tương đương ô đánh dấu X trong biểu mẫu gốc) — ô không áp dụng cho chỉ tiêu đó, bị khóa, không nhập, không hiển thị dạng ô;

(4) API Label — dữ liệu lấy từ API (IRC/GCNĐKĐT hoặc ĐKKD), không cho sửa;

(5) Group header row — row nhóm hoặc tiêu đề, toàn bộ ô data locked, chỉ hiển thị nhãn.

Danh sách nhà đầu tư được lấy tự động từ API theo dự án đã chọn. Nếu dự án có nhiều NĐT, hệ thống hiển thị nhiều block tương ứng. Không cho phép thêm/xóa thủ công.

**PHẦN HEADER — KỲ BÁO CÁO**

| # | Tên trường  | Kiểu trường | Giá trị mặc định              | Được sửa | Bắt buộc | Mô tả/Ghi chú                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ------ | ------------------- | ------------------- | --------------------------------------- | ----------------- | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1 | Quý báo cáo | Read-only       | Theo kỳ báo cáo chọn từ Danh sách |             | x          | Auto-fill từ Kỳ hạn báo cáo tương ứng trên màn hình danh sách. Không cho phép sửa trên form.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 2 | Năm báo cáo | Read-only     | Theo kỳ báo cáo chọn từ Danh sách                    |             | x          | Auto-fill từ Kỳ hạn báo cáo tương ứng trên màn hình danh sách. Không cho phép sửa trên form. |

---

**📌 Phần A: Thông tin chung về dự án đầu tư**

| Mã   | Tên trường                               | Loại cell            | Nguồn dữ liệu | Được sửa | Bắt buộc | Ghi chú                                                                                                                         |
| ----- | ------------------------------------------- | --------------------- | ---------------- | ------------ | ---------- | -------------------------------------------------------------------------------------------------------------------------------- |
| A-001 | Tên dự án / Tên hợp đồng BCC         | Dropdown + Searchable | API              | x            | x          | Hiển thị dạng tĩnh sau khi chọn. Tham chiếu **CMR_12**: Nếu API fail -> trường vẫn là Dropdown (chọn từ danh sách dự án hệ thống) nhưng Enabled để chọn lại, các trường A-002→A-010 giữ Disabled. |
| A-002 | Mã số dự án / Số GCNĐKĐT             | API                   | API              |              |            | Read-only, auto-fill sau khi chọn A-001.                                                                                        |
| A-003 | Ngày cấp (GCNĐKĐT)                      | API                   | API              |              |            | Read-only, auto-fill.                                                                                                            |
| A-004 | Cơ quan cấp GCNĐKĐT                     | API                   | API              |              |            | Read-only.                                                                                                                       |
| A-005 | Địa điểm thực hiện dự án            | API                   | API              |              |            | Read-only.                                                                                                                       |
| A-006 | Tổng vốn đầu tư đăng ký             | API                   | API              |              |            | Read-only. Đơn vị: Triệu VNĐ (phân hệ ĐTTN).                                                   |
| A-007 | Tên tổ chức kinh tế thực hiện dự án | API                   | API              |              |            | Read-only.                                                                                                                       |
| A-008 | Mã số doanh nghiệp / Mã số thuế       | API                   | API              |              |            | Read-only.                                                                                                                       |
| A-009 | Ngày cấp lần đầu (ĐKKD)               | API                   | API              |              |            | Read-only.                                                                                                                       |
| A-010 | Cơ quan cấp Đăng ký kinh doanh         | API                   | API              |              |            | Read-only.                                                                                                                       |
| A-011 | Địa chỉ liên hệ                        | API                   | API              | x            | x          | Cho phép chỉnh sửa vì địa chỉ giao dịch thực tế có thể khác đăng ký.                                             |
| A-012 | Số điện thoại                           | API                   | API              | x            | x          | Cho phép chỉnh sửa trực tiếp. Tham chiếu: CMR_06.                                                                                               |
| A-013 | Email                                       | API                   | API              | x            | x          | Cho phép chỉnh sửa trực tiếp. Tham chiếu: CMR_06.                                                                                               |

---

**📌 Phần B: Tình hình thực hiện dự án đầu tư**

> Cấu trúc eForm Grid — 4 cột dữ liệu: Tên chỉ tiêu | (A) Số liệu thực hiện trong quý báo cáo | (B) Số liệu lũy kế từ đầu năm đến cuối quý báo cáo | (C) Số liệu lũy kế từ khi được cấp GCNĐKĐT đến cuối quý báo cáo

| STT                           | Tên chỉ tiêu                                                         | Loại cell       | Được sửa | Bắt buộc | Cột (A)                     | Cột (B)      | Cột (C)      | Đơn vị | Ghi chú                                                                                                                                            |
| :---------------------------- | :---------------------------------------------------------------------- | :--------------- | :----------- | :--------- | :--------------------------- | :------------ | :------------ | :-------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| **I**                   | **Vốn đầu tư thực hiện **                                        | Auto-calc        |              |            | Σ(A) mục 1,2,3             | Auto-calc     | Auto-calc     | Triệu VNĐ | Group header. Tooltips: (I = 1+2+3)                                                                                                                 |
| 1                             | Vốn góp                                                               | Auto-calc        |              |            | Σ(A) mục 1.1+1.2           | Auto-calc     | Auto-calc     | Triệu VNĐ | Group header. Tooltips: (liệt kê theo từng NĐT)                                                                                                 |
| 1.1                           | Nhà đầu tư Việt Nam                                                | Auto-calc        |              |            | Σ(A) tất cả block NĐT VN | Auto-calc     | Auto-calc     | Triệu VNĐ | Group header.                                                                                                                                       |
| [NĐT VN — row 1]            | [Tên NĐT VN]                                                          | API Label        |              | x          | Σ(A) con                    | Auto-calc     | Auto-calc     | Triệu VNĐ | API IRC (Tham chiếu**CMR_12**). Dữ liệu chỉ lấy từ API, không cho phép thêm/xóa block.                                              |
| [NĐT VN — row 2]            | Mã số thuế: [giá trị MST]                                          | API Label        |              | x          | Locked                       | Locked        | Locked        | —        | Tham chiếu**CMR_12**.                                                                                                                        |
| [NĐT VN — row 3]            | Chia ra:                                                                | Group header     |              |            | Locked                       | Locked        | Locked        | —        | Tiêu đề nhóm.                                                                                                                                   |
| [NĐT VN — row 4]            | - Bằng tiền                                                           | Editable         | x            | x          | Editable                     | Editable      | Editable      | Triệu VNĐ | Nhập tay. Tham chiếu:**CMR_05**.                                                                                                            |
| [NĐT VN — row 5]            | - Máy móc, thiết bị                                                 | Editable         | x            | x          | Editable                     | Editable      | Editable      | Triệu VNĐ | Nhập tay. Tham chiếu:**CMR_05**.                                                                                                            |
| [NĐT VN — row 6]            | - Tài sản khác                                                       | Editable         | x            | x          | Editable                     | Editable      | Editable      | Triệu VNĐ | Nhập tay. Tham chiếu:**CMR_05**.                                                                                                            |
| 1.2                           | Nhà đầu tư nước ngoài                                            | Auto-calc        |              |            | Σ(A) tất cả block NĐT NN | Auto-calc     | Auto-calc     | Triệu VNĐ | Group header.                                                                                                                                       |
| [NĐT NN — row 1]            | [Tên NĐT NN]                                                          | API Label        |              | x          | Σ(A) con                    | Auto-calc     | Auto-calc     | Triệu VNĐ | API IRC (Tham chiếu**CMR_12**). Dữ liệu chỉ lấy từ API, không cho phép thêm/xóa block.                                              |
| [NĐT NN — row 2]            | Mã số thuế/số Quyết định thành lập/số hộ chiếu: [giá trị] | API Label        |              | x          | Locked                       | Locked        | Locked        | —        | Tham chiếu**CMR_12**.                                                                                                                        |
| [NĐT NN — row 3]            | Chia ra:                                                                | Group header     |              |            | Locked                       | Locked        | Locked        | —        | Tiêu đề nhóm.                                                                                                                                   |
| [NĐT NN — row 4]            | - Bằng tiền                                                           | Editable         | x            | x          | Editable                     | Editable      | Editable      | Triệu VNĐ | Nhập tay. Tham chiếu:**CMR_05**.                                                                                                            |
| [NĐT NN — row 5]            | - Máy móc, thiết bị                                                 | Editable         | x            | x          | Editable                     | Editable      | Editable      | Triệu VNĐ | Nhập tay. Tham chiếu:**CMR_05**.                                                                                                            |
| [NĐT NN — row 6]            | - Tài sản khác                                                       | Editable         | x            | x          | Editable                     | Editable      | Editable      | Triệu VNĐ | Nhập tay. Tham chiếu:**CMR_05**.                                                                                                            |
| *(Ghi chú mục 1.2)*         |                                                                          |                   |              |            |                              |               |               |           | Khi dự án không có NĐT nước ngoài: trên eForm ẩn toàn bộ block NĐT NN (mục 1.2). Khi Preview (CF_07.1), In (CF_05), Xuất (CF_04): hiển thị đầy đủ cấu trúc bảng mục 1.2 với giá trị trống. |
| 2                             | Vốn vay                                                                | Auto-calc        |              |            | Σ(A) các dòng vay         | Auto-calc     | Auto-calc     | Triệu VNĐ | Group header. Tooltip (?) RULE-02.                                                                                                                  |
|                               | - Vay trong nước                                                      | Editable         | x            | x          | Editable                     | Editable      | Editable      | Triệu VNĐ | Nhập tay. Tham chiếu:**CMR_05**.                                                                                                            |
|                               | - Vay từ công ty mẹ ở nước ngoài                                 | Editable         | x            | x          | Editable                     | Editable      | Editable      | Triệu VNĐ | Nhập tay. Tham chiếu:**CMR_05**.                                                                                                            |
|                               | - Vay nước ngoài khác                                               | Editable         | x            | x          | Editable                     | Editable      | Editable      | Triệu VNĐ | Nhập tay. Tham chiếu:**CMR_05**.                                                                                                            |
| 3                             | Lợi nhuận tái đầu tư                                              | Editable         | x            | x          | Editable                     | Editable      | Editable      | Triệu VNĐ | Nhập tay. Tham chiếu:**CMR_05**.                                                                                                            |
| **II**                  | **Doanh thu thuần**                                              | Editable         | x            | x          | Editable                     | Editable      | Locked        | Triệu VNĐ | Cột (C) Locked. Tham chiếu:**CMR_05**.                                                                                                      |
| **III**                 | **Giá trị hàng xuất khẩu**                                   | Editable         | x            | x          | Editable                     | Editable      | Locked        | Triệu VNĐ | Tham chiếu:**CMR_05**.                                                                                                                       |
| **IV**                  | **Giá trị hàng nhập khẩu**                                   | Editable         | x            | x          | Editable                     | Editable      | Locked        | Triệu VNĐ | Tham chiếu:**CMR_05**.                                                                                                                       |
| **V**                   | **Số lao động hiện có đến thời điểm báo cáo**                  | Auto-calc        |              |            | Σ(A) LĐ VN + LĐ NN        | Locked        | Locked        | Người   | Cột (B), (C) Locked.                                                                                                                               |
| 1                             | Lao động Việt Nam                                                    | Editable         | x            | x          | Editable                     | Locked        | Locked        | Người   | Tham chiếu:**CMR_05**.                                                                                                                       |
| 2                             | Lao động nước ngoài                                                | Editable         | x            | x          | Editable                     | Locked        | Locked        | Người   | Tham chiếu:**CMR_05**.                                                                                                                       |
| **VI**                  | **Tình hình sử dụng năng lượng**                           | Group header     |              |            | Locked                       | Locked        | Locked        | —        | Group header.                                                                                                                                       |
| 1                             | Điện                                                                  | Editable         | x            | x          | Editable                     | Locked        | Locked        | kWh       | Tham chiếu:**CMR_05**.                                                                                                                       |
| 2                             | Than                                                                    | Editable         | x            | x          | Editable                     | Locked        | Locked        | Tấn      | Tham chiếu:**CMR_05**.                                                                                                                       |
| 3                             | Dầu                                                                    | Editable         | x            | x          | Editable                     | Locked        | Locked        | Lít      | Tham chiếu:**CMR_05**.                                                                                                                       |
| 4                             | Khí LNG                                                                | Editable         | x            | x          | Editable                     | Locked        | Locked        | m³       | Tham chiếu:**CMR_05**.                                                                                                                       |
| 5                             | Các loại năng lượng khác (nếu có)                                     | Editable         | x            |            | Editable                     | Locked        | Locked        | Tự ghi   | Textbox tự do cho tên ĐVT. Tham chiếu:**CMR_05**.                                                                                               |
| **VII**                 | **Thuế và các khoản nộp ngân sách Nhà nước**                   | Editable         | x            | x          | Editable                     | Editable      | Locked        | Triệu VNĐ | Tham chiếu:**CMR_05**.                                                                                                                       |
| **VIII**                | **Diện tích đất, mặt nước đã sử dụng (nếu có)**              | Editable         | x            |            | Editable                     | Editable      | Editable      | m²       | Không bắt buộc. Tham chiếu:**CMR_05**.                                                                                                    |

---

**📌 Phần C: Cập nhật khó khăn, vướng mắc trong quá trình thực hiện dự án (nếu có)**

| Mã   | Tên trường                                                  | Loại cell | Được sửa | Bắt buộc | Ghi chú                                                                                                                                                                          |
| ----- | -------------------------------------------------------------- | ---------- | ------------ | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| C-001 | Khó khăn, vướng mắc, kiến nghị và hướng giải quyết | Textarea   | x            |            | Optional — chữ "(nếu có)" xác nhận không bắt buộc. Placeholder: "Nhập Khó khăn, vướng mắc, kiến nghị và hướng giải quyết (Nêu cụ thể khó khăn, vướng mắc, kiến nghị và hướng giải quyết)". Hỗ trợ xuống dòng. |

---

**📌 Quy tắc Nghiệp vụ Đặc thù (Business Rules)**

| Mã     | Tên quy tắc                           | Mô tả                                                                                                                                                                                                                  |
| ------- | --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| RULE-01 | Quy tắc hiển thị đơn vị báo cáo | Phân hệ ĐTTN: đơn vị mặc định là "Triệu VNĐ" (do dự án ĐTTN được cấp GCNĐKĐT/Quyết định chủ trương đầu tư bằng VNĐ). Riêng mục V (Lao động) dùng "Người", mục VI (Năng lượng) dùng đơn vị riêng (kWh, Tấn, Lít, m³), mục VIII (Diện tích) dùng "m²". |
| RULE-02 | Quy tắc tooltip Vốn vay               | Tại mục "2. Vốn vay" (Phần B), hiển thị tooltip icon `(?)`: "Vốn vay = tổng vay trong kỳ trừ số trả nợ trong kỳ (bao gồm cả vay ngắn hạn, trung hạn và dài hạn)".                               |
| RULE-03 | Quy tắc đổi dự án sau nhập liệu  | Khi người dùng thay đổi dự án (A-001) sau khi đã nhập liệu ở Phần B, hệ thống hiển thị popup cảnh báo P02 (Dirty Form Guard). Nếu người dùng đồng ý đổi -> xóa toàn bộ dữ liệu Phần B. |

---

**CÁC BUTTON**

| #  | Tên           | Kiểu  | Điều kiện hiển thị | Mô tả                                                                     |
| -- | -------------- | ------ | ----------------------- | --------------------------------------------------------------------------- |
| B1 | Hủy           | Button | Luôn                   | Tham chiếu: CF_01 (mục "Xử lý nút [Hủy]").                            |
| B2 | Xem trước | Button | Luôn                   | Preview PDF báo cáo. Tham chiếu: CF_07.1.                                |
| B3 | Lưu nháp     | Button | Luôn                   | Tham chiếu: CF_01 (mục "Xử lý nút [Lưu nháp]").                      |
| B4 | Nộp báo cáo | Button | Luôn                   | Bắt buộc nhập đầy đủ các trường "Bắt buộc". Tham chiếu: CF_01. |

---

### 3. Mô tả các xử lý của chức năng

**Xử lý chung:** Tham chiếu: CF_01 (Lập báo cáo), CMR_18, CF_04 (Xuất báo cáo Excel), CF_05 (In).

- **Nguyên tắc trách nhiệm (API-sourced fields):** Dữ liệu auto-fill từ API chỉ mang tính chất gợi ý/tham khảo. Người dùng tạo báo cáo là người chịu trách nhiệm cuối cùng về nội dung đã nộp — hệ thống cho phép chỉnh sửa tất cả trường API-sourced trước khi Nộp.

**Xử lý đặc thù biểu mẫu A.III.1:**

- **Xử lý Liên động:** Khi người dùng thay đổi Quý báo cáo, hệ thống tự động tính toán lại Năm báo cáo mặc định (chỉ áp dụng khi người dùng chưa chủ động sửa Năm).
- **Xử lý Validation Trùng kỳ (Mã V17):** Kiểm tra trùng (Năm + Quý + Dự án) khi chọn/đổi Dự án tại dropdown A-001, hoặc khi nhấn [Lưu nháp]/[Nộp]. Quý và Năm được xác định tự động từ kỳ hạn đã chọn trên màn hình danh sách (Read-only), do đó trigger Blur trên Quý/Năm không còn áp dụng. Nếu trùng hiển thị lỗi inline và Toast Error: *"Kỳ báo cáo đã tồn tại trong hệ thống. Vui lòng kiểm tra lại."* (Tham chiếu: **list-toast-messages.md**).
- **Xử lý Tính toán (Auto-calc):** Giá trị row "Vốn góp" = Tiền (row 4) + Máy móc (row 5) + Tài sản khác (row 6).
- **Snapshot/Re-fetch dữ liệu NĐT:** Khi Lưu nháp, hệ thống lưu snapshot danh sách NĐT (tên, mã định danh, số block) tại thời điểm đó. Khi Chỉnh sửa, hệ thống re-fetch danh sách NĐT từ API — nếu phát hiện NĐT đã bị xóa khỏi dự án (so với snapshot), hiển thị cảnh báo: *"Nhà đầu tư [Tên NĐT] đã bị xóa khỏi dự án. Vui lòng kiểm tra lại."*
- **Xuất báo cáo:** File xuất là định dạng Excel. **Chỉ từ Màn hình danh sách** (không có trong Preview). Nếu bản ghi có thay đổi chưa Lưu → popup cảnh báo. Tham chiếu: CF_04.

---

## UC221-226.3: Các Tác Vụ Bổ Trợ

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Các tác vụ bổ trợ – Nộp, Nhập từ file, Chỉnh sửa, Xem chi tiết, Xem vòng đời, In, Xuất báo cáo, Xóa

Truy cập chức năng: Màn danh sách báo cáo (UC221-226.1) → Cột Hành động → Chọn tác vụ tương ứng

Chức năng đáp ứng usecase số: 223, 224, 225, 226

---

### 2. Mô tả giao diện

**Các Button theo Action Mapping:**

| # | Tên            | Kiểu  | Điều kiện hiển thị                                                                                                        | Mô tả                                                                        |
| - | --------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| 1 | Nộp            | Button | Chỉ khi Lưu nháp hoặc Yêu cầu chỉnh sửa                                                                                | Tham chiếu: CF_09. Tham chiếu: CF_01 (mục "Xử lý nút [Nộp báo cáo]"). |
| 2 | Nhập từ file          | Button | Trạng thái kỳ = "Trong thời hạn" VÀ (chưa có hồ sơ hoặc hồ sơ ở trạng thái Lưu nháp / Yêu cầu chỉnh sửa) | Tham chiếu: CF_02 Case 1. **Ghi đè:** Nếu bản ghi đã tồn tại (Lưu nháp/YCCS), hiển thị popup cảnh báo ghi đè trước khi nhập từ file. |
| 3 | Chỉnh sửa     | Button | Chỉ khi Lưu nháp hoặc Yêu cầu chỉnh sửa                                                                                | Tham chiếu: CF_03.                                                            |
| 4 | Xem chi tiết   | Button | Tất cả trạng thái                                                                                                          | Mở màn hình xem toàn bộ form (Disabled). Tham chiếu: CF_07.              |
| 5 | Xem vòng đời | Button | Tất cả trạng thái                                                                                                          | Mở popup Vòng đời. Tham chiếu: CF_06.                                     |
| 6 | In              | Button | Tất cả trạng thái                                                                                                          | Tham chiếu: CF_05.                                                            |
| 7 | Xuất báo cáo          | Button | Tất cả trạng thái                                                                                                          | Kết xuất file Excel. **Chỉ từ Màn hình danh sách** (không có trong Preview). Nếu bản ghi có thay đổi chưa Lưu → hiển thị popup: *"Nội dung xuất file là bản đã lưu gần nhất. Vui lòng Lưu nháp trước khi xuất nếu muốn cập nhật."* Tham chiếu: CF_04.                                     |
| 8 | Xóa            | Button | Lưu nháp**VÀ** chưa từng nộp                                                                                       | Tham chiếu: CF_08.                                                            |

---

### 3. Mô tả các xử lý của chức năng

- Nhập từ file: Tham chiếu CF_02. Đặc thù: Nếu đã có hồ sơ Lưu nháp/YCCS cho (Kỳ + Dự án), hệ thống hiển thị popup cảnh báo: *"Dữ liệu hiện tại sẽ bị ghi đè bởi dữ liệu trong file. Bạn có muốn tiếp tục?"* trước khi nhập từ file đè dữ liệu mới.
- Xem chi tiết: Tham chiếu: CF_07.
- Xem vòng đời: Tham chiếu: CF_06.
- In báo cáo: Tham chiếu: CF_05.
- Xuất báo cáo: Kết xuất ra file Excel. **Chỉ từ Màn hình danh sách** (không có trong Preview). Nếu bản ghi có thay đổi chưa Lưu → popup cảnh báo. Tham chiếu: CF_04.
- Chỉnh sửa: Tham chiếu: CF_03.
- Xóa: Tham chiếu: CF_08.

---

## 4. Lịch sử cập nhật

| Ngày      | Phiên bản | Mục cập nhật | Before     | After                                                                                              | Ghi chú                            |
| ---------- | ----------- | --------------- | ----------- | -------------------------------------------------------------------------------------------------- | ------------------------------------ |
| 2026-05-21 | 1.0         | Khởi tạo    | (Không có) | Khởi tạo toàn bộ UC221-226 theo chuẩn Periodic-single, tham chiếu UC041-046 | Init báo cáo theo system_init_workflow |
| 2026-05-21 | 1.0 → 1.1 | UC221-226.2 Mục 3 — V17 Trigger | "Kiểm tra trùng khi Blur trường Năm/Quý hoặc khi nhấn [Lưu nháp]/[Nộp]" | "Kiểm tra trùng khi chọn/đổi Dự án tại dropdown A-001, hoặc khi nhấn [Lưu nháp]/[Nộp]. Quý/Năm Read-only từ màn danh sách." | Q2 audit: Quý/Năm đã là Read-only, trigger Blur không còn áp dụng |
| 2026-05-21 | 1.0 → 1.1 | UC221-226.2 Mục 1 — Preconditions | (Không có) | Bổ sung PRE-01→PRE-04 (đăng nhập, dự án tồn tại, kỳ hạn trong thời hạn, API khả dụng) | Q3 audit: Bổ sung preconditions cho QC setup test data |
| 2026-05-21 | 1.0 → 1.1 | UC221-226.2 Phần B — Block NĐT NN empty state | (Không có) | "Khi không có NĐT NN: eForm ẩn block. Preview/In/Xuất hiển thị đầy đủ cấu trúc bảng với giá trị trống." | Q4 audit: Xác nhận behavior khi không có NĐT nước ngoài |
| 2026-05-21 | 1.0 → 1.1 | UC221-226.2 Phần A — A-012, A-013 | "Cho phép chỉnh sửa trực tiếp." | "Cho phép chỉnh sửa trực tiếp. Tham chiếu: CMR_06." | Q5 audit: Bổ sung tham chiếu validation format theo common rule |
| 2026-05-21 | 1.1 → 1.2 | UC221-226.2 Phần B — Đơn vị eForm Grid | "USD" | "Triệu VNĐ" | ĐTTN luôn dùng VNĐ → đơn vị mặc định là "Triệu VNĐ" |
| 2026-05-21 | 1.1 → 1.2 | RULE-01 | "Đổi toàn bộ Label đơn vị từ USD sang Triệu VNĐ" | "Phân hệ ĐTTN: đơn vị mặc định là Triệu VNĐ" | Không còn conditional — ĐTTN luôn dùng Triệu VNĐ |
| 2026-05-21 | 1.1 → 1.2 | A-006 Ghi chú | "Đơn vị: USD hoặc Triệu VNĐ tùy loại dự án" | "Đơn vị: Triệu VNĐ (phân hệ ĐTTN)" | Cập nhật theo RULE-01 mới |
| 2026-05-22 | 1.2 → 1.3 | Mục 1, 2, 3 | Xóa nội dung phân quyền (Phân quyền: CMR_01/CMR_02/CMR_03) và cột Phân quyền trong bảng Action Mapping, bảng CÁC BUTTON | — | Lược bỏ thông tin phân quyền theo yêu cầu |
