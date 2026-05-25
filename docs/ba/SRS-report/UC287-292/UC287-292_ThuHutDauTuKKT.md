# UC287-292: Tình hình thu hút đầu tư tại khu kinh tế trong kỳ báo cáo (Biểu 2109)

| Thuộc tính | Giá trị |
| --- | --- |
| **BA phụ trách** | hoai.ho |
| **Phân hệ** | KKT/KCN |
| **Mẫu biểu** | Biểu số: 2109.H.QLKKT |
| **Loại báo cáo** | Định kỳ (Quý/Năm) |
| **Hình thức nộp** | Báo cáo đơn lẻ |
| **Cơ quan nhận** | Cục Đầu tư nước ngoài |
| **Giao diện** | Admin site |
| **Đối tượng lập** | Ban Quản lý các khu công nghiệp, kinh tế |
| **Ngày tạo** | 2026-04-27 |
| **Phiên bản** | 1.1 |
| **Phạm vi dữ liệu đầu vào** | Không có phạm vi |
| **Quy tắc sinh mã báo cáo** | EZ_2109HQLKKT_[ID] |

> **Lưu ý kiến trúc:** Báo cáo **định kỳ quý/năm** trên Admin site — danh sách nhóm theo Năm (CS_01, collapsible). Nút [Lập báo cáo] và [Nhập từ file] chỉ hiển thị khi kỳ **Trong thời hạn**. Tham chiếu: CMR_04.
> Đặc thù: Form gồm (1) **Header kỳ báo cáo** auto-fill Disabled; (2) **Hiển thị thành 1 form liền nhau**, người dùng scroll dọc xuống để navigate, gồm 4 phần chính (A/B/C/D); (3) Trong đó phần A và B chia thành các mục I (FDI) và II (DDI), mỗi mục dạng **Matrix 2 cột** (KCN trong KKT | Khu vực khác ngoài KCN); (4) Validate: ≥ 1 phần có dữ liệu khi Nộp; (5) Không có Overview section.
> **Điểm khác biệt A vs B:** Phần A có thêm 2 fields: "Số doanh nghiệp đang hoạt động" (label: "doanh nghiệp") và "Số lao động" (label: "người") — số nguyên dương ≥ 0. Phần B **không có** 2 fields này. Đây là điểm khác biệt duy nhất giữa A và B.

---

## UC287-292.1: Xem Danh Sách Báo Cáo

### 1. Mô tả chức năng

- Tên chức năng: Xem danh sách báo cáo tình hình thu hút đầu tư tại khu kinh tế (Biểu 2109)
- Danh sách nhóm theo Năm. Tham chiếu: CS_01.

Phân quyền: Cán bộ BQL các khu công nghiệp, kinh tế. Tham chiếu: CMR_03.

Truy cập chức năng: Phân hệ Báo cáo KKT/KCN → Tình hình thu hút đầu tư tại KKT (Biểu 2109)

Chức năng đáp ứng usecase số: 287, 288, 289, 290, 291, 292

---

### 2. Mô tả giao diện

**Giao diện danh sách:** Periodic-single, nhóm theo Năm. Tham chiếu: CS_01.

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả |
| --- | --- | --- | --- | --- | --- | --- |
| **Khung Điều kiện Lọc & Tìm kiếm** | | | | | | |
| 1 | Năm | Yearpicker | Năm hiện tại | x | | Người dùng chọn một hoặc nhiều giá trị năm. Lọc theo năm báo cáo. Kết quả lọc hiển thị ngay sau khi chọn. Tham chiếu: CMR_07. |
| 2 | Trạng thái kỳ hạn | Multiple-selection Dropdown | Null | x | | Người dùng chọn một hoặc nhiều giá trị: Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo. Kết quả lọc hiển thị ngay sau khi chọn. Tham chiếu: CMR_04, CMR_07., CMR_16 |
| 3 | Trạng thái báo cáo | Multiple-selection Dropdown | Null | x | | Người dùng chọn một hoặc nhiều giá trị: Lưu nháp / Chờ duyệt / Đã tiếp nhận / Yêu cầu chỉnh sửa. Kết quả lọc hiển thị ngay sau khi chọn. Tham chiếu: CMR_03, CMR_07., CMR_16 |
| 4 | Mã báo cáo | Search bar | Null | x | | Live Search. Tham chiếu: CMR_06, CMR_09. Placeholder: "Tìm kiếm nhanh theo mã báo cáo". |
| **Khung Kỳ hạn (Collapsible)** | | | | | | |
| 5 | Năm báo cáo | Label (collapsible) | Mặc định collapse | | | Tham chiếu: CMR_08. |
| 6 | Trạng thái kỳ hạn | Label | Null | | | Tham chiếu: CMR_04. |
| 7 | Lập báo cáo | Button | Null | | | Trong thời hạn. Tham chiếu: CF_01, CMR_04. |
| 8 | Nhập từ file | Button | Null | | | Trong thời hạn. Tham chiếu: CF_02, CMR_04. |
| **Bảng Danh sách Báo cáo** | | | | | | |
| 9 | Mã báo cáo | Label | Null | | | EZ_2109HQLKKT_[ID]. Tham chiếu: CMR_09. |
| 10 | Ngày cập nhật | Label | Null | | | dd/MM/yyyy HH:mm. |
| 11 | Trạng thái | Label | Null | | | Tham chiếu: CMR_03. |
| 12 | Hành động | Button group | Null | | | Chi tiết: UC287-292.3. |

---

## UC287-292.2: Lập Báo Cáo

### 1. Mô tả chức năng

- Tên chức năng: Tạo mới Báo cáo tình hình thu hút đầu tư tại KKT (Biểu 2109)
- Giao diện **1 form liền nhau**: người dùng scroll dọc xuống để navigate các phần. Gồm 4 phần chính (A, B, C, D), trong đó phần A và B chia thành mục FDI và DDI.

Phân quyền: Cán bộ BQL. Kỳ **Trong thời hạn**. Tham chiếu: CMR_04.

Truy cập chức năng: Màn hình Danh sách → [Lập báo cáo]

Chức năng đáp ứng usecase số: 287, 288

---

### 2. Mô tả giao diện

**BR01 (Định dạng):** Dấu `,` hàng nghìn; dấu `.` thập phân; `/` và `-` cho số hiệu văn bản. Tham chiếu: CMR_05.

**BR02 (Đơn vị vốn theo loại đầu tư):**
- Mục **FDI** (Dự án đầu tư nước ngoài): Label vốn = **"tr.USD"**
- Mục **DDI** (Dự án đầu tư trong nước): Label vốn = **"tỷ VNĐ"**
- Áp dụng cho Fields 4, 6, 8, 10, 13, 14 (thuộc Phần A và B).

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả |
| --- | --- | --- | --- | --- | --- | --- |
| **PHẦN I — THÔNG TIN KỲ BÁO CÁO (Auto-fill, Disabled)** | | | | | | |
| 1 | Quý báo cáo | Label | Auto-fill từ kỳ hạn đã chọn | | | Disabled. Tham chiếu: CMR_08. |
| 2 | Năm báo cáo | Label | Auto-fill từ kỳ hạn đã chọn | | | Disabled. Tham chiếu: CMR_08. |
| **PHẦN II — NỘI DUNG BÁO CÁO (Hiển thị 1 form liền nhau, cuộn dọc)** | | | | | | |
| **A. Tình hình cấp, điều chỉnh và thu hồi các dự án ĐT sản xuất, kinh doanh / B. Tình hình cấp, điều chỉnh và thu hồi các dự án ĐT hạ tầng** | | | | | | |
| **Lưu ý:** Phần A và B có cấu trúc giống nhau, mỗi phần gồm 2 mục con: **I. Dự án đầu tư nước ngoài (FDI)** và **II. Dự án đầu tư trong nước (DDI)**. Cấu trúc của mỗi mục con gồm các chỉ tiêu dưới đây. Tất cả các fields đều là **Required**. Khi ấn CTA (Lưu nháp/Nộp), nếu có trường Required để trống → hiển thị inline error *"Vui lòng nhập [tên trường]"*. **Điểm khác biệt:** Phần A có thêm 2 fields cuối mục ("Số doanh nghiệp đang hoạt động" và "Số lao động") mà Phần B **không có**. Tham chiếu: CMR_05, CMR_06, CMR_07. | | | | | | |
| **Tình hình cấp mới** | | | | | | |
| 3 | Số dự án cấp mới | Number | Null | x | x* | Label: "Dự án". Số nguyên ≥ 0. Tham chiếu: CMR_06. |
| 4 | Tổng vốn ĐT đăng ký mới | Number | Null | x | x* | Label: BR02 (tr.USD/tỷ VNĐ). BR01. Tham chiếu: CMR_06. |
| **Tình hình tăng vốn** | | | | | | |
| 5 | Số dự án tăng vốn | Number | Null | x | x* | Label: "Dự án". Số nguyên ≥ 0. Tham chiếu: CMR_06. |
| 6 | Tổng vốn ĐT tăng | Number | Null | x | x* | Label: BR02. BR01. Tham chiếu: CMR_06. |
| **Tình hình giảm vốn** | | | | | | |
| 7 | Số dự án giảm vốn | Number | Null | x | x* | Label: "Dự án". Số nguyên ≥ 0. Tham chiếu: CMR_06. |
| 8 | Tổng vốn ĐT giảm | Number | Null | x | x* | Label: BR02. BR01. Tham chiếu: CMR_06. |
| **Tình hình thu hồi/chấm dứt** | | | | | | |
| 9 | Số dự án thu hồi/chấm dứt | Number | Null | x | x* | Label: "Dự án". Số nguyên ≥ 0. Tham chiếu: CMR_06. |
| 10 | Tổng vốn thu hồi/chấm dứt | Number | Null | x | x* | Label: BR02. BR01. Tham chiếu: CMR_06. |
| **Biến động diện tích đất** | | | | | | |
| 11 | Biến động quy mô DT đất cho thuê | Number | Null | x | x* | Label: "ha". BR01. Có thể âm. Tham chiếu: CMR_06. |
| **Lũy kế đến cuối kỳ** | | | | | | |
| 12 | Số dự án (lũy kế) | Number | Null | x | x* | Label: "Dự án". Số nguyên ≥ 0. Tham chiếu: CMR_06. |
| 13 | Tổng vốn ĐT đăng ký (lũy kế) | Number | Null | x | x* | Label: BR02. BR01. Tham chiếu: CMR_06. |
| 14 | Tổng vốn ĐT thực hiện (lũy kế) | Number | Null | x | x* | Label: BR02. BR01. Tham chiếu: CMR_06. |
| 15 | Tổng quy mô DT đất đã cho thuê (lũy kế) | Number | Null | x | x* | Label: "ha". BR01. Tham chiếu: CMR_06. |
| **Chỉ áp dụng cho Phần A (không có ở Phần B)** | | | | | | |
| 15a | Số doanh nghiệp đang hoạt động | Number | Null | x | x* | Label: "doanh nghiệp". Số nguyên dương ≥ 0. Không cho phép số âm, không cho phép thập phân. **Chỉ có ở Phần A.** Tham chiếu: CMR_05, CMR_06. |
| 15b | Số lao động | Number | Null | x | x* | Label: "người". Số nguyên dương ≥ 0. Không cho phép số âm, không cho phép thập phân. **Chỉ có ở Phần A.** Tham chiếu: CMR_05, CMR_06. |
| **C. Tình hình sản xuất kinh doanh của các dự án đầu tư** | | | | | | |
| **Lưu ý:** Validate: Nếu nhập bất kỳ ô nào → toàn phần Required. | | | | | | |
| 16 | Doanh thu | Number | Null | x | x* | Label: "tr.USD". Cố định. BR01. Tham chiếu: CMR_06. |
| 17 | Giá trị nhập khẩu | Number | Null | x | x* | Label: "tr.USD". Cố định. BR01. Tham chiếu: CMR_06. |
| 18 | Giá trị xuất khẩu | Number | Null | x | x* | Label: "tr.USD". Cố định. BR01. Tham chiếu: CMR_06. |
| 19 | Nộp ngân sách | Number | Null | x | x* | Label: "tỷ VNĐ". Cố định. BR01. Tham chiếu: CMR_06. |
| **D. Lao động** | | | | | | |
| **Lưu ý:** Validate: Nếu nhập bất kỳ ô nào → Fields 21-22 Required. | | | | | | |
| 20 | Tổng số lao động | Label (Disabled) | Tự tính | | | Auto-calc = Field 21 + Field 22. Real-time. Label: "người". |
| 21 | Tổng số lao động trong nước | Number | Null | x | x* | Label: "người". Số nguyên ≥ 0. Tham chiếu: CMR_06. |
| 22 | Tổng số lao động nước ngoài | Number | Null | x | x* | Label: "người". Số nguyên ≥ 0. Tham chiếu: CMR_06. |
| **Các Button** | | | | | | |
| 23 | Hủy | Button | | | | Luôn Enabled. Tham chiếu: CF_01. |
| 24 | Xem trước | Button | | | | Luôn Enabled. Popup PDF Preview. Tham chiếu: CF_07.1. |
| 25 | Lưu nháp | Button | | | | Luôn Enabled. Tham chiếu: CF_01. |
| 26 | Nộp báo cáo | Button | | | | Luôn Enabled. Validate: ≥ 1 section có dữ liệu. Tham chiếu: CF_01, CMR_18. |

---

### 3. Mô tả các xử lý của chức năng

**Auto-fill Header Kỳ báo cáo:** Quý/Năm Disabled, lấy từ kỳ hạn đã chọn ở màn danh sách. Tham chiếu: CMR_08.

**Điều hướng form:**
- Form hiển thị liền nhau, người dùng scroll dọc xuống để navigate qua các phần A, B, C, D.
- Người dùng có thể chủ động đóng/mở (collapsible) các phần nếu cần.
- Dirty Form Guard chỉ kích hoạt khi user điều hướng ra khỏi màn hình lập/sửa báo cáo (nhấn [Hủy], breadcrumb, sidebar...). Tham chiếu: CMR_14.

**Validate Required:**
- Tất cả các fields trong mỗi section đều là **Required**.
- Khi nhấn CTA (Lưu nháp / Nộp), nếu có trường Required bị bỏ trống → hiển thị inline error màu đỏ *"Vui lòng nhập [tên trường]"* bên dưới trường tương ứng. Tự động biến mất khi người dùng nhập giá trị hợp lệ. Tham chiếu: CMR_05, CMR_06, CMR_07.
- Khi Nộp: Tổng số fields có dữ liệu (trên toàn bộ form) ≥ 1. Nếu không có dữ liệu nào → báo lỗi *"Vui lòng khai báo ít nhất 1 chỉ tiêu"*. Tham chiếu: CF_01.
- **Fields 15a, 15b (Chỉ Phần A):** "Số doanh nghiệp đang hoạt động" và "Số lao động" — chỉ chấp nhận số nguyên dương (≥ 0). Không cho phép số âm, không cho phép thập phân. Nếu nhập ký tự không hợp lệ (dấu trừ, dấu chấm thập phân) → inline error *"Ký tự không hợp lệ. Chỉ chấp nhận chữ số, dấu chấm và dấu phẩy"*. Tham chiếu: CMR_05.

**BR02 — Đơn vị tiền tệ theo Mục:**
- Mục FDI: Hiển thị label "tr.USD" trên tiêu đề cột các fields vốn (Fields 4, 6, 8, 10, 13, 14 của Phần A và B).
- Mục DDI: Hiển thị label "tỷ VNĐ" tại các vị trí tương ứng.
- Phần C (Fields 16-19): Label cố định.

**Auto-calculate Field 18 (Tổng lao động):** = Field 19 + Field 20. Áp dụng độc lập cho từng cột (KCN trong KKT và Khu vực khác). Disabled, real-time.

---

## UC287-292.3: Các Tác Vụ Bổ Trợ

### 1. Mô tả chức năng

- Tên chức năng: Các tác vụ bổ trợ — Xem chi tiết, Chỉnh sửa, Nộp, Xem vòng đời, In, Xuất báo cáo, Xóa
- Phân quyền: Cán bộ BQL (Người tạo). Tham chiếu: CMR_03.

Truy cập chức năng: Màn danh sách báo cáo (UC287-292.1) → Cột Hành động

Chức năng đáp ứng usecase số: 289, 290, 291, 292

---

### 2. Mô tả giao diện

| # | Tên | Kiểu | Điều kiện hiển thị | Phân quyền | Mô tả |
| --- | --- | --- | --- | --- | --- |
| 1 | Nộp | Button | Lưu nháp & Yêu cầu chỉnh sửa | Người tạo | Luôn Enabled. Tham chiếu: CF_09. Tham chiếu: CF_01, CMR_18. |
| 2 | Chỉnh sửa | Button | Lưu nháp & Yêu cầu chỉnh sửa | Người tạo | Luôn Enabled. Tham chiếu: CF_03. |
| 3 | Xem chi tiết | Button | Tất cả trạng thái | Người tạo | Luôn Enabled. Tham chiếu: CF_07. Hiển thị form liền nhau gồm 4 phần. |
| 4 | Xem vòng đời | Button | Tất cả trạng thái | Người tạo | Luôn Enabled. Tham chiếu: CF_06. |
| 5 | In | Button | Tất cả trạng thái | Người tạo | Luôn Enabled. Tham chiếu: CF_05. |
| 6 | Xuất báo cáo | Button | Tất cả trạng thái | Người tạo | Luôn Enabled. Kết xuất **.docx**. Tham chiếu: CF_04. |
| 7 | Xóa | Button | Lưu nháp **VÀ** chưa từng nộp | Người tạo | Luôn Enabled. Tham chiếu: CF_08. |

---

### 3. Mô tả các xử lý của chức năng

- Xem chi tiết (CF_07): Hiển thị form liền nhau, tất cả các phần ở trạng thái Read-only. Chỉ expand các phần/mục có dữ liệu, collapse rỗng.
- Chỉnh sửa: Tham chiếu CF_03.
- Nộp từ Màn hình danh sách: Tham chiếu CF_09.
- Xuất báo cáo (.docx): Tham chiếu CF_04.
- Xóa: Tham chiếu CF_08.

---

---

## 4. Lịch sử cập nhật

| Ngày | Phiên bản | Mục cập nhật | Before | After | Ghi chú |
| --- | --- | --- | --- | --- | --- |
| 2026-05-03 | N/A | Trạng thái báo cáo | Đã nộp | Chờ duyệt / Đã tiếp nhận | Thay đổi theo bộ trạng thái mới của hệ thống (CMR_03) |
| 2026-05-11 | +1 | Tên cột | `Ngày cập nhật / Nộp` | `Ngày cập nhật` | Đồng bộ tên cột theo CS_02 (INS-03) |
| 2026-05-17 | CMR v2.0 | Placeholder Search bar (1 dong) | Nhap du lieu | Tim kiem nhanh theo ma bao cao | Chuan hoa CMR_06 v2.0 STD-04b |
| 2026-05-17 | CMR v2.0 | Them tham chieu CMR_16 (2 dong filter dropdown) | Chua co CMR_16 | Them , CMR_16 sau CMR_07 tren cac dong Multiple-selection Dropdown | Filter dropdown phai co option Tat ca (CMR_16) |
| 2026-05-17 | CMR v2.0 | STD-02 Required message trong AC/logic | Truong bat buoc | Vui long nhap/chon [ten truong] | Dong bo CMR v2.0 |
| 2026-05-18 | CMR v2.0 -> 2.1 | Thuật ngữ nút bấm | Export / Import | Xuất báo cáo / Nhập từ file | Cập nhật đồng bộ tiếng Việt |
| 2026-05-21 | 1.0 → 1.1 | Thêm 2 fields Section A + xác nhận cấu trúc form | Section A và B giống nhau hoàn toàn | Section A có thêm "Số doanh nghiệp đang hoạt động" (label: doanh nghiệp) và "Số lao động" (label: người) — số nguyên dương ≥ 0. Section B không có 2 fields này. | Q3 Answer — BA xác nhận Phương án A (continuous form + accordion) + bổ sung 2 fields cho Section A |
| 2026-05-22 | Align CMR | Bổ sung "Luôn Enabled" cho tất cả Button; Thêm CMR_18 vào Nộp báo cáo (CF_01); Xác nhận Numeric precision 15+5 | Buttons chưa ghi "Luôn Enabled"; Nộp chưa có CMR_18 | Tất cả Button ghi "Luôn Enabled"; Nộp báo cáo tham chiếu CF_01, CMR_18 | Align CMR Report — Đồng bộ quy tắc chung |

---

## BỔ SUNG: TOAST / ERROR / INLINE MESSAGES (Cập nhật 2026-05-22)

> Nguồn tham chiếu: CMR_common_business_rules.md, CF_common_functions.md, list-toast-messages.md, Check_CMR_UC239-298_Toast_Error_Inline_20260522_v1.md

### 1. Toast Messages

| Mã | Trường hợp | Tiêu đề | Nội dung | Loại | Áp dụng CF |
| :--- | :--- | :--- | :--- | :--- | :--- |
| T01 | Lập báo cáo + Lưu nháp thành công | Thành công | Đã lập báo cáo thành công | 🟢 Success | CF_01 |
| T02 | Nộp báo cáo thành công | Thành công | Đã nộp báo cáo thành công | 🟢 Success | CF_01, CF_03, CF_09 |
| T03 | Chỉnh sửa báo cáo + Lưu nháp thành công | Thành công | Đã chỉnh sửa báo cáo thành công | 🟢 Success | CF_03 |
| T04 | Xuất báo cáo thành công | Thành công | Đã xuất báo cáo thành công | 🟢 Success | CF_04, CF_07 |
| T05 | Lỗi hệ thống (API fail, lưu/nộp/xuất fail) | Lỗi hệ thống | Không thể kết nối đến hệ thống. Vui lòng thử lại sau | 🔴 Error | CF_01–CF_09 |
| T07 | Lưu nháp khi tất cả trường đều trống | Lưu nháp không thành công | Bạn cần nhập dữ liệu cho trường thông tin trước khi lưu nháp | 🔴 Error | CF_01, CF_03 |
| T08 | Xóa báo cáo thành công | Thành công | Xóa báo cáo thành công | 🟢 Success | CF_08 |

> **Lưu ý:** Tất cả message KHÔNG có dấu `.` ở cuối câu.

### 2. Inline Validation Messages

#### 2.1. Required Fields

| Loại trường | Message lỗi | Vị trí hiển thị | Tham chiếu CMR |
| :--- | :--- | :--- | :--- |
| Trường số (Numeric) bắt buộc bỏ trống | `"Vui lòng nhập [tên trường]"` | Bên dưới trường, màu đỏ | CMR_05 |
| Trường text bắt buộc bỏ trống | `"Vui lòng nhập [tên trường]"` | Bên dưới trường, màu đỏ | CMR_06 |
| Dropdown bắt buộc chưa chọn | `"Vui lòng chọn [tên trường]"` | Bên dưới trường, màu đỏ | CMR_07 |

**Trong eForm Grid:** Lỗi hiển thị dạng viền đỏ quanh ô + tooltip khi hover.

#### 2.2. Numeric Validation

| Trường hợp | Message lỗi | Tham chiếu | Ghi chú |
| :--- | :--- | :--- | :--- |
| Nhập ký tự không hợp lệ (chữ cái, ký tự đặc biệt ngoài `-`, `.`, `,`) | `"Ký tự không hợp lệ. Chỉ chấp nhận chữ số, dấu chấm, dấu phẩy và dấu trừ"` | CMR_05, V02 | Áp dụng tất cả trường số |
| Trường yêu cầu ≥ 0: nhập dấu trừ `-` | `"Ký tự không hợp lệ. Chỉ chấp nhận chữ số, dấu chấm và dấu phẩy"` | CMR_05, V03 | **KHÔNG áp dụng cho Field 11 "Biến động diện tích"** (cho phép âm) |
| Sai cấu trúc số (nhiều dấu chấm, dấu phẩy sai vị trí) | `"Sai định dạng số"` | CMR_05, V04 | Áp dụng tất cả trường số |
| Vượt giới hạn digit precision | `"[Tên trường] chỉ được nhập tối đa 15 chữ số phần nguyên và 5 chữ số phần thập phân"` | Align_CMR C05b | Áp dụng tất cả trường số |

> **Lưu ý đặc biệt:** Field 11 "Biến động diện tích" cho phép nhập giá trị **ÂM** (dấu trừ `-`). Áp dụng V02 (chấp nhận dấu trừ), KHÔNG áp dụng V03 cho field này.

#### 2.3. V16 — Form rỗng khi Nộp

| Trường hợp | Message lỗi |
| :--- | :--- |
| Form không có dữ liệu chỉ tiêu nào khi nhấn Nộp | `"Vui lòng khai báo ít nhất 1 chỉ tiêu trong kỳ báo cáo"` |

### 3. Popup Messages

| Mã | Trường hợp | Tiêu đề | Nội dung | Nút | Tham chiếu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| P01 | Xác nhận trước khi nộp | Bạn có chắc muốn nộp? | Checkbox: "Tôi đã kiểm tra toàn bộ thông tin đã nhập và xác nhận rằng các thông tin đó là chính xác" | [Xác nhận] / [Hủy] / ✕ | CF_01, CF_03 |
| P02 | Dirty Form Guard — dữ liệu chưa lưu | Dữ liệu chưa được lưu | Bạn có chắc chắn muốn rời khỏi trang này không? | [Đồng ý] / [Hủy] | CMR_14 |
| P04 | Xác nhận trước khi xóa | — | Bạn có chắc chắn muốn xóa báo cáo này? | [Đồng ý] / [Hủy] | CF_08 |

### 4. Quy tắc Numeric Digit Precision (Bổ sung)

Áp dụng cho **TẤT CẢ** trường số trong UC287-292:
- Phần nguyên: tối đa **15 chữ số**
- Phần thập phân: tối đa **5 chữ số**
- Tổng tối đa: 21 ký tự (bao gồm dấu phân cách)
- Khi vượt giới hạn → block nhập thêm + hiển thị inline error

### 5. Tham chiếu CMR/CF bắt buộc

| Rule | Mô tả |
| :--- | :--- |
| CMR_04 | Trạng thái kỳ hạn báo cáo |
| CMR_05 | Quy tắc trường số (15+5 digit precision) |
| CMR_06 | Quy tắc trường text |
| CMR_07 | Quy tắc dropdown |
| CMR_12 | Trường auto-fill từ API |
| CMR_14 | Dirty Form Guard |
| CMR_15 | Thêm/Xóa hàng bảng động |
| CMR_16 | Filter Dropdown "Tất cả" |
| CMR_18 | Tab Navigation |
| CF_01 | Lập báo cáo |
| CF_02 | Nhập từ file |
| CF_03 | Chỉnh sửa |
| CF_04 | Xuất báo cáo |
| CF_06 | Xem vòng đời |
| CF_07 | Xem chi tiết |
| CF_08 | Xóa báo cáo |
| CF_09 | Nộp từ Danh sách |
