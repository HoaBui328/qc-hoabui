# UC239-244: Tình hình thu hút đầu tư vào khu công nghiệp trong kỳ báo cáo (Biểu 2101)

| Thuộc tính                            | Giá trị                                      |
| --------------------------------------- | ---------------------------------------------- |
| **BA phụ trách**                | hoai.ho                                        |
| **Phân hệ**                     | KKT/KCN                                        |
| **Mẫu biểu**                    | Biểu 2101.H.QLKKT                             |
| **Loại báo cáo**               | Định kỳ (Quý / Năm)                       |
| **Hình thức nộp**              | Báo cáo đơn lẻ                            |
| **Cơ quan nhận**                | Cục Đầu tư nước ngoài                   |
| **Giao diện**                    | Admin site                                     |
| **Đối tượng lập**            | Ban Quản lý các khu công nghiệp, kinh tế |
| **Ngày tạo**                    | 2026-04-27                                     |
| **Phiên bản**                   | 1.1                                            |
| **Phạm vi dữ liệu đầu vào** | Không có phạm vi                            |
| **Quy tắc sinh mã báo cáo**   | EZ_2101HQLKKT_[ID]                             |

> **Lưu ý kiến trúc:** Báo cáo **định kỳ quý/năm** trên Admin site — danh sách nhóm theo Năm (CS_01, collapsible). Nút [Lập báo cáo] và [Nhập từ file] chỉ hiển thị khi kỳ **Trong thời hạn**, ẩn khi Chưa tới hạn hoặc Qua kỳ báo cáo (Tham chiếu: CMR_04).
> Đặc thù: Layout tạo báo cáo dạng **E-form Ma trận (Matrix)** với 4 cột vị trí khu vực cố định. Màn hình được chia thành 2 tab Dự án FDI - với các trường điền giá trị số tỷ giá là "tr.USD" và Dự án DDI - với các trường điền giá trị số tỷ giá là "tỷ VNĐ". Cả 2 tab đều có chung 1 cấu trúc form từ field của mục 1 "Tình hình cấp mới" đến mục 6 "Tình hình sản xuất kinh doanh", chỉ khác nhau về tỷ giá tiền. Hỗ trợ tính tổng tự động theo hàng ngang.

---

## UC239-244.1: Xem Danh Sách Báo Cáo

### 1. Mô tả chức năng

- Tên chức năng: Xem danh sách báo cáo tình hình thu hút đầu tư vào KCN (Biểu 2101.H.QLKKT)
- Chức năng cho phép Cán bộ Ban Quản lý xem danh sách các báo cáo định kỳ. Danh sách được nhóm theo Năm (collapsible). Tham chiếu: CS_01.

Phân quyền: Cán bộ Ban Quản lý các khu công nghiệp, kinh tế. Mỗi tài khoản chỉ quản lý và nhìn thấy các bản ghi do mình tạo (Tham chiếu: CMR_03).

Truy cập chức năng: Phân hệ Báo cáo KKT/KCN → Thu hút đầu tư KCN (Biểu 2101)

Chức năng đáp ứng usecase số: 239, 240, 241, 242, 243, 244

---

### 2. Mô tả giao diện

**Giao diện danh sách:** Periodic-single, nhóm theo Năm. Tham chiếu: CS_01.

| #                                              | Tên trường          | Kiểu trường              | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả                                                                                                                                                                                          |
| ---------------------------------------------- | ---------------------- | --------------------------- | --------------------- | ------------ | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Khung Điều kiện Lọc & Tìm kiếm** |                        |                             |                       |              |            |                                                                                                                                                                                                  |
| 1                                              | Năm                   | Yearpicker                  | Năm hiện tại       | x            |            | Người dùng chọn một hoặc nhiều giá trị năm. Lọc theo năm báo cáo. Khi ấn chọn giá trị lọc tương ứng, kết quả lọc hiển thị ngay. Tham chiếu: CMR_07.                 |
| 2                                              | Trạng thái kỳ hạn  | Multiple-selection Dropdown | Null                  | x            |            | Người dùng chọn một hoặc nhiều giá trị: Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo. Kết quả lọc hiển thị ngay sau khi chọn. Tham chiếu: CMR_04, CMR_07., CMR_16              |
| 3                                              | Trạng thái báo cáo | Multiple-selection Dropdown | Null                  | x            |            | Người dùng chọn một hoặc nhiều giá trị: Lưu nháp / Chờ duyệt / Đã tiếp nhận / Yêu cầu chỉnh sửa. Kết quả lọc hiển thị ngay sau khi chọn. Tham chiếu: CMR_03, CMR_07., CMR_16 |
| 4                                              | Mã báo cáo          | Search bar                  | Null                  | x            |            | Live Search. Tham chiếu: CMR_06, CMR_09. Placeholder: "Tìm kiếm nhanh theo mã báo cáo".                                                                                                                        |
| **Khung Kỳ hạn (Collapsible)**         |                        |                             |                       |              |            |                                                                                                                                                                                                  |
| 5                                              | Năm báo cáo         | Button (collapsible)        | Mặc định collapse  |              |            | VD: "Năm 2026". Click → expand danh sách kỳ. Tham chiếu: CMR_08.                                                                                                                            |
| 6                                              | Trạng thái kỳ hạn  | Label                       | Null                  |              |            | Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo. Tham chiếu: CMR_04.                                                                                                                     |
| 7                                              | Lập báo cáo         | Button                      | Null                  |              |            | Chỉ hiển thị khi kỳ ở trạng thái**Trong thời hạn**. Ẩn khi Chưa tới hạn hoặc Qua kỳ báo cáo. Tham chiếu: CF_01, CMR_18, CMR_04.                                                  |
| 8                                              | Nhập từ file                 | Button                      | Null                  |              |            | Chỉ hiển thị khi kỳ ở trạng thái**Trong thời hạn**. Ẩn khi Chưa tới hạn hoặc Qua kỳ báo cáo. Tham chiếu: CF_02, CMR_04.                                                  |
| **Bảng Danh sách Báo cáo**           |                        |                             |                       |              |            |                                                                                                                                                                                                  |
| 9                                              | Mã báo cáo          | Label                       | Null                  |              |            | EZ_2101HQLKKT_[ID]. Tham chiếu: CMR_09.                                                                                                                                                         |
| 10                                             | Ngày cập nhật       | Label                       | Null                  |              |            | Định dạng: dd/MM/yyyy HH:mm.                                                                                                                                                                  |
| 11                                             | Trạng thái           | Label                       | Null                  |              |            | Trạng thái bản ghi. Tham chiếu: CMR_03.                                                                                                                                                      |
| 12                                             | Hành động           | Button group                | Null                  |              |            | Chi tiết: UC239-244.3.                                                                                                                                                                          |

---

### 3. Mô tả các xử lý của chức năng

- Danh sách nhóm theo Năm (collapse mặc định). Sắp xếp năm mới nhất lên trên. Tham chiếu: CS_01, CMR_10.
- Nút [Lập báo cáo] và [Nhập từ file] chỉ hiển thị khi kỳ **Trong thời hạn**. Tham chiếu: CMR_04.
- Tất cả bộ lọc hiển thị kết quả ngay lập tức. Tham chiếu: CMR_07.

---

## UC239-244.2: Lập Báo Cáo

### 1. Mô tả chức năng

- Tên chức năng: Tạo mới Báo cáo thu hút đầu tư vào KCN (Biểu 2101.H.QLKKT)
- Chức năng cho phép Cán bộ BQL nhập liệu dưới dạng E-form Ma trận. Báo cáo được chia thành 2 tab Dự án FDI - với các trường điền giá trị số tỷ giá là "tr.USD" và Dự án DDI - với các trường điền giá trị số tỷ giá là "tỷ VNĐ". Hệ thống tự động tính tổng theo hàng ngang và hỗ trợ quy đổi tỷ giá. Tham chiếu: CF_01, CMR_18.

Phân quyền: Cán bộ BQL các khu công nghiệp, kinh tế (Admin site). Kỳ hạn phải ở trạng thái **Trong thời hạn**. Tham chiếu: CMR_04.

Truy cập chức năng: Màn danh sách báo cáo (UC239-244.1) → Nhấn nút [Lập báo cáo]

Chức năng đáp ứng usecase số: 239, 240

---

### 2. Mô tả giao diện

**Giao diện E-form Ma trận (Matrix Layout)**

Form thiết kế dạng bảng với:

- **Cột Trái (Chỉ tiêu):** Hiển thị tên các chỉ tiêu nhập liệu (Rows).
- **Cột Nhập liệu (Vị trí khu vực):** 4 cột cố định cho phép điền giá trị.
  1. KCN nằm ngoài KKT
  2. KCN nằm trong KKT ven biển
  3. KCN nằm trong KKT cửa khẩu
  4. KCN nằm trong KKT chuyên biệt
- **Cột Tổng cộng:** Tính tổng tự động (sum ngang) của 4 cột vị trí. Disabled.
- Section "Tình hình kinh doanh của các dự án đầu tư"
  1. Layout hiển thí: Section này sẽ được dùng chung cho cả 2 tab, hiển thị không bị ảnh hưởng hay reload lại bởi hành động chuyển tab của người dùng. Section này sẽ được đặt ở cuối trang, dưới bảng form báo cáo. Sẽ làm được hiển thị dưới dạng 1 persistent summary section (Cross-tab aggregated, sticky summary panel). Bao gồm các field sau:
     * Doanh thu, hiển thị label **"tỷ VNĐ"**
     * Giá trị nhập khẩu, hiển thị label **"tỷ VNĐ"**
     * Giá trị xuất khẩu, hiển thị label: **"tỷ VNĐ"**
     * Nộp ngân sách, hiển thị label: **"tỷ VNĐ"**
  2. Hiển thị logic:
     * Doanh thu: Tính tổng của trường "Doanh thu" trong bảng form báo cáo từ 2 tab
     * Giá trị nhập khẩu: Tính tổng của trường "Giá trị nhập khẩu" trong bảng form báo cáo từ 2 tab
     * Giá trị xuất khẩu: Tính tổng của trường "Giá trị xuất khẩu" trong bảng form báo cáo từ 2 tab
     * Nộp ngân sách: Tính tổng của trường "Nộp ngân sách" trong bảng form báo cáo từ 2 tab

**Business Rules chung:**

- **BR01 (Định dạng số):** Sử dụng dấu `,` phân tách hàng nghìn, dấu `.` phân tách thập phân. (Tham chiếu: CMR_05).
- **BR02 (Đơn vị tiền tệ):**
  - Phần I (Dự án FDI): Các trường số tiền mặc định hiển thị nhãn **"tr.USD"**.
  - Phần II (Dự án DDI): Các trường số tiền mặc định hiển thị nhãn **"tỷ VNĐ"**.

| Cấu trúc Form                                               | Mô tả & Validation (Áp dụng cho 4 cột vị trí)                                                                                                                                                   | Cột Tổng cộng                        |
| ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------- |
| **TAB 1: DỰ ÁN ĐẦU TƯ NƯỚC NGOÀI (FDI)**        | Các chỉ tiêu tiền tệ hiển thị label**"tr.USD"** (BR02)                                                                                                                                          |                                         |
| **1. Tình hình cấp mới**                            |                                                                                                                                                                                                        |                                         |
| - Số dự án                                                 | Textbox (Number). Required. Validate: ≥ 0. Label: "Dự án".                                                                                                                                          | Label (Calculated sum).                 |
| - Tổng vốn đầu tư đăng ký mới                        | Textbox (Number). Required. Validate: ≥ 0. Label: "tr.USD".                                                                                                                                           | Label (Calculated sum).                 |
| **2. Tình hình tăng vốn**                           |                                                                                                                                                                                                        |                                         |
| - Số dự án                                                 | Textbox (Number). Required. Validate: ≥ 0. Label: "Dự án".                                                                                                                                          | Label (Calculated sum).                 |
| - Tổng vốn đầu tư tăng                                  | Textbox (Number). Required. Validate: ≥ 0. Label: "tr.USD".                                                                                                                                           | Label (Calculated sum).                 |
| **3. Tình hình giảm vốn**                           |                                                                                                                                                                                                        |                                         |
| - Số dự án                                                 | Textbox (Number). Required. Validate: ≥ 0. Label: "Dự án".                                                                                                                                          | Label (Calculated sum).                 |
| - Tổng vốn đầu tư giảm                                  | Textbox (Number). Required. Validate: ≥ 0. Label: "tr.USD".                                                                                                                                           | Label (Calculated sum).                 |
| **4. Tình hình thu hồi/chấm dứt HĐ**              |                                                                                                                                                                                                        |                                         |
| - Số dự án                                                 | Textbox (Number). Required. Validate: ≥ 0. Label: "Dự án".                                                                                                                                          | Label (Calculated sum).                 |
| - Tổng vốn ĐT thu hồi/chấm dứt                          | Textbox (Number). Required. Validate: ≥ 0. Label: "tr.USD".                                                                                                                                           | Label (Calculated sum).                 |
| **5. Biến động quy mô diện tích đất cho thuê** |                                                                                                                                                                                                        |                                         |
| - Biến động diện tích                                    | Textbox (Number). Required. Validate: Cho phép số âm/dương. Label: "ha".`<br>`Có tooltip hiển thị "Tổng diện tích cho thuê - tổng diện tích thu hồi" khi hover con trỏ chuột vào. | Label (Calculated sum).                 |
| **6. Tình hình sản xuất kinh doanh**                |                                                                                                                                                                                                        |                                         |
| - Doanh thu                                                   | Textbox (Number). Required. Validate: ≥ 0. Label: "tr.USD".`<br>`**Có Inline message:** *"Quy đổi sang VNĐ: [Giá trị] tỷ VNĐ"*                                                      | Label (Calculated sum).                 |
| - Giá trị nhập khẩu                                       | Textbox (Number). Required. Validate: ≥ 0. Label: "tr.USD".`<br>`**Có Inline message:** *"Quy đổi sang VNĐ: [Giá trị] tỷ VNĐ"*                                                      | Label (Calculated sum).                 |
| - Giá trị xuất khẩu                                       | Textbox (Number). Required. Validate: ≥ 0. Label: "tr.USD".`<br>`**Có Inline message:** *"Quy đổi sang VNĐ: [Giá trị] tỷ VNĐ"*                                                      | Label (Calculated sum).                 |
| - Nộp ngân sách                                            | Textbox (Number). Required. Validate: ≥ 0. Label: "tr.USD".`<br>`*(Không có inline message quy đổi)*                                                                                          | Label (Calculated sum).                 |
| **TAB 2: DỰ ÁN ĐẦU TƯ TRONG NƯỚC (DDI)**         | Các chỉ tiêu tiền tệ hiển thị label**"tỷ VNĐ"** (BR02). Không có inline message quy đổi tỷ giá ở toàn bộ Tab 2. Cấu trúc chỉ tiêu (1 → 6) lặp lại y hệt Tab 1.               | Label (Calculated sum) cho từng dòng. |

**Các Nút Hành Động:**

- **[Lưu nháp]**: Tham chiếu CF_01.
- **[Xem trước]**: Popup PDF Preview. Tham chiếu CF_07.1.
- **[Nộp báo cáo]**: Tham chiếu CF_01.
- **[Hủy]**: Tham chiếu CF_01.


**CÁC BUTTON**

| #  | Tên           | Kiểu   | Điều kiện hiển thị | Phân quyền       | Mô tả                                                                                |
| -- | -------------- | ------- | ----------------------- | -------------------- | ------------------------------------------------------------------------------------- |
| B1 | Hủy           | Button | Luôn                   | Người tạo         | Tham chiếu: CF_01, CMR_18 (mục "Xử lý nút [Hủy]").                                     |
| B2 | Xem trước | Button | Luôn                   | Người tạo         | Mở popup PDF Preview báo cáo (không rời màn Lập). Tham chiếu: CF_07.1.        |
| B3 | Lưu nháp     | Button | Luôn                   | Người tạo         | Tham chiếu: CF_01, CMR_18 (mục "Xử lý nút [Lưu nháp]").                                |
| B4 | Nộp báo cáo | Button | Lưu nháp, Yêu cầu CS | Người tạo         | Validate toàn bộ trường bắt buộc trước khi nộp. Tham chiếu: CF_01, CMR_18.         |
---



### 3. Mô tả các xử lý của chức năng

**Xử lý Form Ma trận:**

- Toàn bộ form được hiển thị trên cùng 1 trang, cuộn dọc từ Phần I xuống Phần II.
- Cột "Tổng cộng" ngoài cùng bên phải sẽ tự động tính tổng (Sum) giá trị của 4 cột nhập liệu tương ứng trên cùng 1 hàng ngang. Cập nhật real-time. Label cột tổng trùng với Label cột nhập liệu.

**Xử lý Inline Message Quy đổi Tỷ giá (Tab 1 - FDI):**

- Áp dụng cho 3 trường: Doanh thu, Giá trị nhập khẩu, Giá trị xuất khẩu.
- **Nguồn tỷ giá:** Lấy tự động qua API của Ngân hàng Nhà nước (NHNN) **tại thời điểm lập báo cáo** (lần đầu nhấn [Lập báo cáo]). Tỷ giá này được **lưu cùng bản ghi** và sử dụng xuyên suốt vòng đời báo cáo (từ lúc lập → chỉnh sửa → nộp).
- **Giá trị quy đổi:** Được tính toán và **lưu cùng bản ghi** tại thời điểm lập. Công thức: `Giá trị quy đổi = (Giá trị nhập vào (tr.USD) × Tỷ giá đã lưu) / 1000` (đơn vị: tỷ VNĐ).
- Hiển thị Text mờ bên dưới ô input dạng: *"Quy đổi sang VNĐ: 12.5 tỷ VNĐ (Tỷ giá: [Giá trị tỷ giá đã lưu])"*.
- Nếu API NHNN lỗi hoặc không lấy được tỷ giá **tại thời điểm lập**: Inline message hiển thị *"Quy đổi sang VNĐ: Không thể lấy tỷ giá"*. Cho phép lưu nháp mà không có tỷ giá; khi mở lại chỉnh sửa, hệ thống thử gọi lại API 1 lần nếu chưa có tỷ giá.
- **Lưu ý:** Khi user thay đổi giá trị input (VD: Doanh thu), hệ thống tính lại giá trị quy đổi bằng tỷ giá đã lưu (không gọi lại API).

**Validate khi Nộp:**

- Toàn bộ các ô input trong ma trận đều là trường Required. Nếu KCN không có phát sinh, người dùng phải nhập `0`.
- Bắt lỗi định dạng số và số thập phân theo BR01.

---

## UC239-244.3: Các Tác Vụ Bổ Trợ

### 1. Mô tả chức năng

- Tên chức năng: Các tác vụ bổ trợ — Xem chi tiết, Chỉnh sửa, Nộp, Xem vòng đời, In, Xuất báo cáo, Xóa
- Phân quyền: Cán bộ BQL (Người tạo). Quản lý theo quyền tác giả, các tài khoản khác không thấy bản ghi này. Tham chiếu: CMR_03. Không áp dụng CMR_01/CMR_02.

Truy cập chức năng: Màn danh sách báo cáo (UC239-244.1) → Cột Hành động

Chức năng đáp ứng usecase số: 241, 242, 243, 244

---

### 2. Mô tả giao diện

**Màn hình Xem chi tiết:** Tham chiếu: CF_07.
Hiển thị layout Ma trận giống hệt màn hình tạo mới nhưng tất cả ô input đều Disabled (chỉ đọc). Vẫn hiển thị các inline message quy đổi (theo tỷ giá thời điểm tạo/sửa gần nhất).

**UI Behavior — Sticky Header:**
- Header row của bảng Ma trận (dòng chứa tên các cột: Chỉ tiêu, KCN nằm ngoài KKT, KCN trong KKT ven biển, KCN trong KKT cửa khẩu, KCN trong KKT chuyên biệt, Tổng cộng) sẽ **sticky** (cố định) khi người dùng cuộn dọc trang.
- Khi scroll xuống, header row giữ nguyên vị trí ở đầu vùng hiển thị bảng để người dùng luôn biết đang xem cột nào.
- Áp dụng cho cả màn hình Xem chi tiết và màn hình Chỉnh sửa.

**Action Mapping (Màn hình Xem chi tiết):**

| # | Tên            | Kiểu  | Điều kiện hiển thị                  | Phân quyền | Mô tả                                                                                                 |
| - | --------------- | ------ | ---------------------------------------- | ------------ | ------------------------------------------------------------------------------------------------------- |
| 1 | Quay lại       | Button | Tất cả trạng thái                    | Người tạo | Quay lại màn danh sách báo cáo.                                                                       |
| 2 | Xuất báo cáo   | Button | Tất cả trạng thái                    | Người tạo | Kết xuất báo cáo. Tham chiếu: CF_04.                                                                 |
| 3 | Chỉnh sửa     | Button | Lưu nháp & Yêu cầu chỉnh sửa       | Người tạo | Tham chiếu: CF_03.                                                                                     |
| 4 | Nộp báo cáo    | Button | Lưu nháp & Yêu cầu chỉnh sửa       | Người tạo | Tham chiếu: CF_09. Tham chiếu: CF_01, CMR_18.                                                                 |

> **Lưu ý:** Khi trạng thái = "Chờ duyệt" hoặc "Đã tiếp nhận", chỉ hiển thị [Quay lại] và [Xuất báo cáo]. Không cho phép Chỉnh sửa hoặc Nộp lại.

**Action Mapping (Màn hình Danh sách):**

| # | Tên            | Kiểu  | Điều kiện hiển thị                  | Phân quyền | Mô tả                                                                                                 |
| - | --------------- | ------ | ---------------------------------------- | ------------ | ------------------------------------------------------------------------------------------------------- |
| 1 | Nộp            | Button | Lưu nháp & Yêu cầu chỉnh sửa       | Người tạo | Tham chiếu: CF_09. Tham chiếu: CF_01, CMR_18.                                                                 |
| 2 | Chỉnh sửa     | Button | Lưu nháp & Yêu cầu chỉnh sửa       | Người tạo | Tham chiếu: CF_03.                                                                                     |
| 3 | Xem chi tiết   | Button | Tất cả trạng thái                    | Người tạo | Tham chiếu: CF_07.                                                                                     |
| 4 | Xem vòng đời | Button | Tất cả trạng thái                    | Người tạo | Tham chiếu: CF_06.                                                                                     |
| 5 | In              | Button | Tất cả trạng thái                    | Người tạo | Tham chiếu: CF_05.                                                                                     |
| 6 | Xuất báo cáo          | Button | Tất cả trạng thái                    | Người tạo | Kết xuất**.docx**. Layout matrix cần đảm bảo không vỡ khung khi xuất Word. Tham chiếu: CF_04. |
| 7 | Xóa            | Button | Lưu nháp**VÀ** chưa từng nộp | Người tạo | Tham chiếu: CF_08.                                                                                     |

---

### 3. Mô tả các xử lý của chức năng

- Xem chi tiết: Tham chiếu CF_07.
- Chỉnh sửa: Tham chiếu CF_03. Tỷ giá quy đổi (inline message) sẽ sử dụng **tỷ giá đã được lưu cùng bản ghi tại thời điểm lập báo cáo**, không gọi lại API. Khi user thay đổi giá trị input, hệ thống tính lại giá trị quy đổi bằng tỷ giá đã lưu.
- Nộp từ Màn hình danh sách: Tham chiếu CF_09.
- Xem vòng đời: Tham chiếu CF_06.
- In: Tham chiếu CF_05.
- Xuất báo cáo (.docx): Tham chiếu CF_04. Cần lưu ý xử lý dàn trang ngang (landscape) khi xuất Word do bảng có nhiều cột.
- Xóa: Tham chiếu CF_08.

---

## 4. Lịch sử cập nhật

| Ngày      | Phiên bản | Mục cập nhật                  | Before                        | After                          | Ghi chú                                                       |
| ---------- | ----------- | -------------------------------- | ----------------------------- | ------------------------------ | -------------------------------------------------------------- |
| 2026-05-03 | N/A         | Trạng thái báo cáo           | Đã nộp                     | Chờ duyệt / Đã tiếp nhận | Thay đổi theo bộ trạng thái mới của hệ thống (CMR_03) |
| 2026-05-08 | 1.0 → 1.1  | Kiểu trường filter Dropdown   | Multiple choice dropdown list | Multiple-selection Dropdown    | Chuẩn hóa tên component theo CMR_07, CMR_16                         |
| 2026-05-11 | +1          | Tên cột                        | `Ngày cập nhật / Nộp`   | `Ngày cập nhật`           | Đồng bộ tên cột theo CS_02 (INS-03)                       |
| 2026-05-11 | +1          | Dòng phân cách bảng Markdown | Thiếu cột (1 chỗ)          | Đủ số cột theo header      | Chuẩn hóa separator (INS-05)                                 |
| 2026-05-13 | +1          | Màn Xem chi tiết — Sticky header | Không có | Header row sticky khi scroll dọc | Theo kết quả design review UC239-250 |
| 2026-05-13 | +1          | Action Mapping — Tách riêng Xem chi tiết vs Danh sách | Chung 1 bảng | Tách 2 bảng: Xem chi tiết chỉ có [Quay lại][Xuất][Sửa][Nộp]; Danh sách giữ nguyên | Theo BA comment: bỏ nút "Xem" trên trang xem chi tiết, chuẩn hóa logic nút theo trạng thái |
| 2026-05-17 | CMR v2.0 | Placeholder Search bar (1 dong) | Nhap du lieu | Tim kiem nhanh theo ma bao cao | Chuan hoa CMR_06 v2.0 STD-04b |
| 2026-05-17 | CMR v2.0 | Them tham chieu CMR_16 (3 dong filter dropdown) | Chua co CMR_16 | Them , CMR_16 sau CMR_07 tren cac dong Multiple-selection Dropdown | Filter dropdown phai co option Tat ca (CMR_16) |
| 2026-05-17 | CMR v2.0 | Them tham chieu CMR_18 (Tab Navigation) | Chua co CMR_18 | Them CMR_18 vao tham chieu CF_01 | Tuan thu CMR_18 Tab Navigation tren form nhap lieu |
| 2026-05-18 | CMR v2.0 -> 2.1 | Thuật ngữ nút bấm | Export / Import | Xuất báo cáo / Nhập từ file | Cập nhật đồng bộ tiếng Việt |

---

## BỔ SUNG: TOAST / ERROR / INLINE MESSAGES (Cập nhật 2026-05-22)

> Tham chiếu: CMR_05, CMR_06, CMR_07, CF_01, CF_03, CF_04, CF_07, CF_08, CF_09, list-toast-messages.md

### 1. Toast Messages

| Mã | Trường hợp | Tiêu đề | Nội dung | Loại |
| :--- | :--- | :--- | :--- | :--- |
| T01 | Lập báo cáo + Lưu nháp thành công | Thành công | Đã lập báo cáo thành công | 🟢 Success |
| T02 | Nộp báo cáo thành công | Thành công | Đã nộp báo cáo thành công | 🟢 Success |
| T03 | Chỉnh sửa + Lưu nháp thành công | Thành công | Đã chỉnh sửa báo cáo thành công | 🟢 Success |
| T04 | Xuất báo cáo thành công | Thành công | Đã xuất báo cáo thành công | 🟢 Success |
| T05 | Lỗi hệ thống (API fail, lưu/nộp/xuất fail) | Lỗi hệ thống | Không thể kết nối đến hệ thống. Vui lòng thử lại sau | 🔴 Error |
| T07 | Lưu nháp khi tất cả trường đều trống | Lưu nháp không thành công | Bạn cần nhập dữ liệu cho trường thông tin trước khi lưu nháp | 🔴 Error |
| T08 | Xóa báo cáo thành công | Thành công | Xóa báo cáo thành công | 🟢 Success |

### 2. Inline Validation Messages

| Trường hợp | Message | Vị trí | Tham chiếu |
| :--- | :--- | :--- | :--- |
| Trường số bắt buộc bỏ trống | "Vui lòng nhập [tên trường]" | Bên dưới trường, màu đỏ | CMR_05 |
| Trường text bắt buộc bỏ trống | "Vui lòng nhập [tên trường]" | Bên dưới trường, màu đỏ | CMR_06 |
| Dropdown bắt buộc chưa chọn | "Vui lòng chọn [tên trường]" | Bên dưới trường, màu đỏ | CMR_07 |
| Nhập ký tự không hợp lệ vào trường số | "Ký tự không hợp lệ. Chỉ chấp nhận chữ số, dấu chấm, dấu phẩy và dấu trừ" | Bên dưới trường, màu đỏ | CMR_05, V02 |
| Trường số ≥ 0: nhập dấu trừ | "Ký tự không hợp lệ. Chỉ chấp nhận chữ số, dấu chấm và dấu phẩy" | Bên dưới trường, màu đỏ | CMR_05, V03 |
| Sai cấu trúc số (nhiều dấu chấm, dấu phẩy sai) | "Sai định dạng số" | Bên dưới trường, màu đỏ | CMR_05, V04 |
| Vượt digit precision (>15 nguyên hoặc >5 thập phân) | "[Tên trường] chỉ được nhập tối đa 15 chữ số phần nguyên và 5 chữ số phần thập phân" | Bên dưới trường, màu đỏ | Align_CMR C05b |
| Bảng rỗng khi Nộp (không có dữ liệu) | "Vui lòng khai báo ít nhất 1 KCN trong kỳ báo cáo" | Inline error hoặc Toast | V16 |

**Lưu ý eForm Grid:** Trong lưới nhập liệu, lỗi hiển thị dạng **viền đỏ** quanh ô + **tooltip** chứa message lỗi khi hover (do không gian hạn chế).

### 3. Popup Messages

| Mã | Trường hợp | Tiêu đề | Nội dung | Nút |
| :--- | :--- | :--- | :--- | :--- |
| P01 | Xác nhận nộp báo cáo | Bạn có chắc muốn nộp? | Checkbox: "Tôi đã kiểm tra toàn bộ thông tin đã nhập và xác nhận rằng các thông tin đó là chính xác" | [Xác nhận] / [Hủy] / ✕ |
| P02 | Dirty Form Guard | Dữ liệu chưa được lưu | Bạn có chắc chắn muốn rời khỏi trang này không? | [Đồng ý] / [Hủy] |
| P04 | Xác nhận xóa báo cáo | — | Bạn có chắc chắn muốn xóa báo cáo này? | [Đồng ý] / [Hủy] |

### 4. Quy tắc Numeric (Bổ sung theo Align_CMR)

- **Digit precision:** Phần nguyên tối đa **15 chữ số**, phần thập phân tối đa **5 chữ số**. Tổng max length = 21 ký tự (15 + 1 dấu `.` + 5).
- **Áp dụng cho:** Tất cả trường Number trong form (Số dự án, Tổng vốn, Diện tích, Doanh thu, v.v.)
- **Trường "Biến động diện tích":** Cho phép số âm (dấu `-` ở đầu). Các trường khác: chỉ ≥ 0.
- **Error khi vượt:** "[Tên trường] chỉ được nhập tối đa 15 chữ số phần nguyên và 5 chữ số phần thập phân"

> **Lưu ý format:** Toàn bộ error/toast/inline message KHÔNG có dấu `.` ở cuối câu.
